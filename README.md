# BYU IS 455 API EXAMPLES

This repository is meant to serve as an example for creating a machine learning model from a dataset then deploying it to a web application as an API that can be connected to a front-end application. I have included a front-end example using React to connect with the backends. I have built 3 different backend examples.

1. Flask - Flask is a minimal Python web framework that is more customizable and has less overhead than Django. This would be my preference for creating an API considering you only really need one Python file to make it.
2. Django - A lot of you are probably familiar with Django, since we are only using one route for the API it can be a bit burdensome considering it is using an entire framework for one route. But if it is a preferred framework there is an example for you.
3. C# ASP.NET 6 - I built the backend API in ASP.NET 6, this version is in the event you want to use C# as your backend. You will have to use a different file format when exporting your created model, this is a ONNX file that generally works better with C#.

Each example has its own instructions.txt file should should provide a good overview of commands to run, libraries to include, and the process of building an API for our purposes.
