Eagle Eye - Eye Disease Detection

This project, named "Eagle Eye," is designed to detect eye diseases from an eye image. It utilizes a pretrained deep learning model to classify the images. This README will provide information on how the application works and how to use it.
Prerequisites

Before running the application, make sure you have the following installed on your system:

    Python
    The required Python libraries listed in the requirements.txt file.

To use it, upload the code to Git and create a new Streamlit app linked to this Git repository.
Getting Started

    Launch the application, and it will display an eye-catching background and the title "Eagle Eye."

    Click the "Browse" button or drag and drop an image of your eye from your computer. Ensure that the image is in JPEG, JPG, or PNG format.

    The application will load the image you selected and display it.

    After a brief moment, the application will provide a diagnosis for the eye image, indicating whether it's "Healthy" or shows signs of disease.

    A confidence score is also displayed to indicate the model's confidence in its prediction.

    If the model detects that the eye is "Healthy," a smiling emoji will be displayed to signify that everything is fine.

That's it! You have now successfully used the "Eagle Eye" application to detect eye diseases from an eye image.
Notes

    The application uses a model of your choice, you can change it if you change "detectmaladie.h5". Don't change the name. Ensure that the model is loaded correctly and that the classes of eye diseases are defined in the "labels.txt" file.

    The model may not be perfect and may produce incorrect results. It is recommended to consult a healthcare professional for reliable medical diagnoses.

    You can customize the background by replacing the image located in the "fondecran" directory.
