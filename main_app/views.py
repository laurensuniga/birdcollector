# package for generating unique keys for the photos
import uuid
# AWS SKD package
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Bird, Toy, Photo
from .forms import FeedingForm

# format should be `protocol://service-code.region-code.amazonaws`
S3_BASE_URL = 'https://s3.us-west-1.amazonaws.com/'
BUCKET = 'lauren-nexus-catcollector'

class BirdCreate(CreateView):
  model = Bird
  fields = ['name', 'breed', 'description', 'age']

class BirdUpdate(UpdateView):
  model = Bird
  fields = ['breed', 'description', 'age']

class BirdDelete(DeleteView):
  model = Bird
  success_url = '/birds/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def birds_index(request):
  birds = Bird.objects.all()
  return render(request, 'birds/index.html', { 'birds': birds })

def birds_detail(request, bird_id):
  bird = Bird.objects.get(id=bird_id)
  # exclude from our query all toys associated w/ the current cat
  toys_bird_doesnt_have = Toy.objects.exclude(id__in = bird.toys.all().values_list('id'))
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'birds/detail.html', {
    # pass the cat and feeding_form as context
    'bird': bird, 'feeding_form': feeding_form,
    'available_toys': toys_bird_doesnt_have
  })

def add_feeding(request, bird_id):
	# create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.bird_id = bird_id
    new_feeding.save()
  return redirect('detail', bird_id=bird_id)

def assoc_toy(request, bird_id, toy_id):
  # locate the cat & add the toy by its ID
  Bird.objects.get(id=bird_id).toys.add(toy_id)
  return redirect('detail', bird_id=bird_id)


def add_photo(request, bird_id):
    # the <input> will have `name` attribute - thats the key our file will be
    photo_file = request.FILES.get('photo_file', None)

    if photo_file:
        # creat and s3 instance
        s3 = boto3.client('s3')

        # generate a unique "key" for the image
        # variable to store the index of the dot before file extension
        # rfind will find the last instance of the '.' character
        index_of_last_period = photo_file.name.rfind('.')
        # generate a unique key and grab the first 6 characters
        # G4F&8F.png
        key = uuid.uuid4().hex[:6] + photo_file.name[index_of_last_period:]

        try:
            # s3 client - attempt to perform a file upload
            s3.upload_fileobj(photo_file, BUCKET, key)

            # Generate the URL based on the key name, our base url, bucket
            url = f"{S3_BASE_URL}{BUCKET}/{key}"

            photo = Photo(url= url, bird_id=bird_id)
            photo.save()
        except:
            print('An error occurred uploading files to AWS')

    return redirect('detail', bird_id=bird_id)


class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'