<h1>style="text-align: center">COOK BOOK</h1>

<p>The goal of the project is to create a website based on a data base that executes CRUD operation on data base.</p>
<p>The goal of the website is create a huge data base with recipes from all around the word where everyone can look for a recipe or upload one.</p>


<h2>UX</h2>

<p>The website is made for everyone who want to find recipes from all around the word and wants to share his cooking knowladge with others.</p>
<p>Through this website the user can view the collection of recipes from data base on landing page, can search by name, country, type or if is suitable for vegan due to the search box.</p>
<p>The recipes are displayed as card with 3 buttons wherewith user can like or dislike the recipe and to view the recipe in details.</p>
<p>Details page offers details in deep about recipe and the possibility to perform action on the recipe like edit, delete and like/dislike the recipe.</p>
<p>The add page offers the possibility to insert a new recipe through the form provided where user can set a name, photo, a description, the origin of the recipe, type, ingredients need it, cooking steps, tools, the source and if is suitable for vegans.<p>
<p>The edit page has same structure as add page the difference is that the fields are auto filled with the details of the current recipe and updates the current recipe instead of creating a new one.</p>
<p>About page offers couple details about the porpoise of the website, features, developer, offer the possibility to send ideas of improvement and feedback through the form provided and details about updates that are comming up.</p>

<h2>Features</h2>

<h3>Existing Features</h3>
<ol>
    <li>CRUD operation</li>
    <li>Optimized for Search</li>
    <li>Easy to Use</li>
    <li>Responsive Web Design</li>
</ol>
<h4>1 - CRUD operation</h4>
<p>User can:</p>
<ul>
<li> create a recipe by filling the form from add recipe page</li>
<li> view the collection of recipes by visiting the lading page</li>
<li> edit a recipe by pressing edit button from recipe details page</li>
<li> delete a recipe by pressing the delete button from recipe details page</li>
</ul>

<h4>2 Responsive Web Design</h4>
<p>The website is builded to meet the requirements of nowadays displaying devices:</p>
<ul>
<li>it is responsive for mobile phone, table and desktop</li>
<li>it has a simplified design for mobile phone user due to the side navigation where user can search or go on different webpages </li>
</ul>

<h3>Features Left to Implement</h3> 
<ul>
    <li>Comment section for every recipe</li>
    <li>A forum where users can discus topic opened by them</li>
    <li>A side chat where users can have chats with other visitors of webpage</li>
    <li>A shop where users can buy cooking tools like pans, plates etc</li>
</ul>

<h2>Technologies Used</h2> 
<ol>
    <li>Html and Css: for creating the structure and the design of webpage</li>
    <li>JavaScript: for DOM manipulation</li>
    <li>Python, Flask Framework: for creating a reliable, scalable, and maintainable web application and for performing CRUD operation on database </li>
    <li>Materializecss: for design</li>
</ol>


<h2>Testing</h2>
<p>The webpage use forms for search, editing and inserting recipes in database</p>
<p>To test:</p>
<ol>
    <li>Search form:
        <ul>
            <li>I tried to submit empty form and check if displays all recipes as intended</li>
            <li>I tried to search separately by name, country, type, suitable for vegans</li>
            <li>I tried to search same by name, country, type, suitable for vegans and check if displays the recipes with characteristics provided</li>
        </ul>
    </li>
    <li>Edit and Add form:
        <ul>
            <li>I tried to submit empty form and verify that an error message about the required fields appears.</li>
        </ul>
    </li>
    <li>Responsive:
        <ul>
            <li>By using Google Chrome Developer Tools to test the look and the functionability on Iphone X as sizemark for mobile, Ipad for table and my monitor resolution (1337x768) for desktop view</li>
        </ul>
    </li>
</ol>
<p>Problems:</p>
<ol>
    <li>Search form:
        <ul>
            <li>Trying to iterate 2 times throughout the fields of a document in the same template I found out it doesn't work. That means that it iterates just one time throughout the document and second time it will get nothing from the document's fields, so I decided to duplicate the variables that get the lists of countries and types until I find another way to do that</li>
        </ul>
    </li>
</ol>


<h2>Deployment</h2>
<p>The project is deployed with heroku</p>
<p>To  do that I had to:</p>
<ul>
    <li>create an app on heroku</li>
    <li>login on heroku from gitpod</li>
    <li>create a procfile and requirements.txt</li>
    <li>upload everything on heroku</li>
    <li>and set the environment variables</li>
</ul>
<p>If you want to run the code locally you have to:</p>
<ul>
    <li>create a workspace with gitpod</li>
    <li>install through the terminal Flask, Flask_pymongo and dnspython</li>
    <li>run the app.py</li>
    <li>open the "port 8080" from "Open Ports" Tab</li>
</ul>
<p>Or you can click on this <a href="https://cook-idea.herokuapp.com/">Cook Book</a></p>

<h2>Credits</h2> 

<h3>Content</h3> 
<p>Every recipe has a source from where everyting was copied</p>
<h3>Media</h3>
<p>The photos from recipes cards are linked by user through link inserted.</p>
<h3>Acknowledgements</h3> 
<p>None</p>