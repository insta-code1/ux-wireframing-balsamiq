## 1.0 Bootstrap Tutorial for Beginners

The following are the step by step guide to your first web development with Bootstrap.

### Step 1: Download or Include Bootstrap

You can [download bootstrap here](http://getbootstrap.com/getting-started/#download), but in this guide we will just use the bootstrap CDN.

It means that we will not have to download and store the bootstrap files to our server or local machine. We will just include the bootstrap CSS and JavaScript links to our page.

### Step 2: Write Basic HTML Code

Our basic HTML code will have the following. We name our file index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>

	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">

	<title>Live Demo of Bootstrap Tutorial for Beginners</title>

</head>
<body>

</body>
</html>

``` 


### Step 3: Include Bootstrap CSS

It will be inside the ‘head’ tag and under ‘title’ tag.

```html
<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css">
``` 


### Step 4: Include jQuery Library

Yes, we still have jQuer here. This for bootstrap functions that needs jQuery. If you want to learn more about jQuery, I have this <a>useful tutorial here</a>.

Include the jQuery library before the ending ‘body’ tag.

```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
``` 


### Step 5: Include Bootstrap JavaScript

Bootstrap has JavaScript source code for some reasons like animation and other functions for a better user experience.

```html
<script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
``` 


### Step 6: Add IE8 support for HTML5 and media queries

Bootstrap 3 is also a framework that is highly concerned with the mobile arena. It is responsive to different devices and screen sizes.

```html
<!--[if lt IE 9]>
<script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
<script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
<![endif]-->
``` 


### Step 7: Add a Navigation Bar

Navigation bars are so cool and can let your users know they won’t get lost on your website. It is also used for easy access of functions or commonly used pages and buttons.

```html
<div class="navbar navbar-default navbar-static-top" role="navigation">
	<div class="container">

		<div class="navbar-header">
			<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
			<span class="sr-only">Toggle navigation</span>
			<span class="icon-bar"></span>
			<span class="icon-bar"></span>
			<span class="icon-bar"></span>
			</button>
			<a class="navbar-brand" href="http://mikspot.com/" title='Your choice, your world!'>Home</a>
		</div>

		<div class="navbar-collapse collapse">
			<ul class="nav navbar-nav">
				<li class="active">
					<a href="#">All</a>
				</li>
				<li>
					<a href="#">Demo</a>
				</li>
				<li>
					<a href="#">Contact</a>
				</li>
			</ul>
		</div><!--/.nav-collapse -->

	</div>
</div>
``` 


### Step 8: Add Page Content Container.

This ‘div’ will contain and hold our web site content. It is important because it defines the width of our content page so it won’t scatter the content when the user has large screen size.

under navigation

```html
<div class="container">

</div>
``` 


### Step 9: Add a Heading

The heading is important since it tells the user what page he was in and what is it for.

```html
<div class="page-header">
	<h1>Bootstrap Sample Page with Form</h1>
</div>
``` 


### Step 10\. Add a Table

In this example, we have a table that will hold form elements like a text box later. The bootstrap table looks good, has hover effect and is also responsive.

```html
<table class='table table-hover table-responsive table-bordered'>

	<tr>
		<td>Name</td>
		<td></td>
	</tr>

	<tr>
		<td>Contact Number</td>
		<td></td>
	</tr>

	<tr>
		<td>Address</td>
		<td></td>
	</tr>

	<tr>
		<td>List</td>
		<td>
		</td>
	</tr>

	<tr>
		<td></td>
		<td>

		</td>
	</tr>

</table>
``` 


### Step 11: Add a Form Inside a Table

This is what I was talking about at step 10\. Our form example includes few text boxes, a text area and select drop-down list.

```html
<form action='http://demo.codeofaninja.com/tutorials/bootstrap-tutorial-for-beginners/' method='post'>

	<table class='table table-hover table-responsive table-bordered'>

		<tr>
			<td>Name</td>
			<td><input type='text' name='name' class='form-control' required></td>
		</tr>

		<tr>
			<td>Contact Number</td>
			<td><input type='text' name='contact_number' class='form-control' required></td>
		</tr>

		<tr>
			<td>Address</td>
			<td><textarea name='address' class='form-control'></textarea></td>
		</tr>

		<tr>
			<td>List</td>
			<td>
				<select name='list_id' class='form-control'>
					<option value='1'>List One</option>
					<option value='2'>List Two</option>
					<option value='3'>List Three</option>
				</select>
			</td>
		</tr>

		<tr>
			<td></td>
			<td>
			</td>
		</tr>

	</table>
</form>
``` 


### Step 12: Add a Bootstrap Button with Glyphicon

Glyphicons is a library of precisely prepared monochromatic icons and symbols, created with an emphasis on simplicity and easy orientation.

Buttons with icons look cute. Well, at least for me. It also signals the user what the button is for. Button icon and color can easily tell what the button does in your web app.

```html
<button type="submit" class="btn btn-primary">
	<span class="glyphicon glyphicon-plus"></span> Create New Record
</button>
``` 


## Step 13: Add a Good Looking Message Box

You can also add some notes in a nice way using bootstrap.

```html
<div class="alert alert-info">
	<strong>Heads up!</strong> This bootstrap page example is from Mike Dalisay of <a href="http://codeofaninja.com/">codeofaninja.com</a>!
</div>
``` 
