# Music Better

```bash
python manage.py runserver
```

After changing models:

```bash
python manage.py makemigrations
python manage.py migrate
```

To create superuser:

```bash
python manage.py createsuperuser
```
(follow instructions in console)
go to /admin/ url to log in

## Deploying to The Cloud
Build & Migrate: `gcloud builds submit --config cloudmigrate.yaml --substitutions _INSTANCE_NAME=music-better,_REGION=us-central1`

Deploy: `gcloud run deploy music-better --platform managed --region us-central1 --image gcr.io/musicbetter/polls-service --add-cloudsql-instances musicbetter:us-central1:music-better --allow-unauthenticated`