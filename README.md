# gallery_app
 
Architecture Diagram
 
Overview of Project
For the final project, we built upon the prior assignments to have a fully functional photo storage gallery.  Our project URL is https://gallery-app-main-53ww5vlwvq-uc.a.run.app/
and the project ID is mygallery-375619 on Google Cloud Platform. The GitHub repository is located at https://github.com/phaneendra2429/gallery_app-main. 
The website first greets the user with a sign-in page. A new user can create their account and see a blank dashboard and existing users can enter their credentials and see their stored photos. Once a user uploads a photo it will be visible on the page. A user can click or tap on the image to view its metadata. From either the main page or the metadata page, a user can download or delete an image. When a user deletes the photo, it will remove it from their account. A user can access their photos from any device or web browser with their credentials.
	For this project, we created a website using Flask and HTML and originally hosted the photos on a Virtual Machine. We then moved the data to be stored in Google Cloud Storage buckets using BLOB storage and integrated Firebase to account for user logins. The project is hosted using Google Cloud Platform and deploys as a Cloud Run service using the Cloud Build API that connects to our GitHub repository. Use privacy is handled by only allowing a user to access their records instead of the public. By using Google Firebase we ensure security through their storage and encryption of login credentials to eliminate a potential hack or data leak.

Information Stored  
	The information that is collected and stored are the images uploaded and their respective metadata. That information is stored as a BLOB in Google Cloud Storage and Datastore. A folder is created for each user that signs up to the application and uploads a photo. You can see each user that has access to the application and if you click on a user, their uploaded photos will show as well as their respective metadata. The BLOB storage is organized in Google Cloud 
Storage where we have a bucket “proj2_phani” that houses objects for each user which stores the photos for their account and Datastore saves the metadata of the images. We then use Google Firebase for the authentication of our sign-ins, where it validates the user exists and has entered the correct credentials. 

Project Demo
To access the application navigate to https://gallery-app-main-53ww5vlwvq-uc.a.run.app/. 
User Registration/Login
To register for an account, select Sign Up from the homepage 

Fill in your email and password you want to use for the Gallery App.
If your account already exists, you’ll be prompted to login 

Once logged in you will be greeted with your image dashboard where you can view the images uploaded. 
To upload an image, select Choose File on the top right of the page.

You will be prompted to choose a photo you want to upload from your device. Once you select a photo, the file name will appear instead of “No File Chosen” and you may select Upload.
Once the image is uploaded, it will appear in your dashboard alongside your other images. View Metadata
In order to view the metadata of your image, select it on your dashboard. 

You will be directed to a new page that shows the image, its name, and its metadata.
Image Download
You can download an image two ways:
On the dashboard, press the Download button

On the metadata page, press the Download button

Image Deletion
You can delete an image two ways:
On the dashboard, press the Delete button


On the metadata page, press the Delete button

You will receive a pop-up asking you to confirm you want to delete the image. When you select yes, you will be brought back to the dashboard with the chosen image deleted.

