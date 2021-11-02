# QA Automation scripts

This aims to simplify and guide beginners to run the tests and/or make their first contribution. 

## Running Scripts on Local Machine

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### If you don't have git on your machine, [install it](https://help.github.com/articles/set-up-git/).

### Fork this repository

Fork this repository by clicking on the fork button on the top of this page.
This will create a copy of this repository in your account.

### Clone the repository

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Now clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the code button and then click the _copy to clipboard_ icon.

Open a terminal and run the following git command:

```
git clone "url you just copied"
```

where "url you just copied" (without the quotation marks) is the url to this repository (your fork of this project). See the previous steps to obtain the url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

For example:

```
git clone https://github.com/this-is-you/first-contributions.git
```

where `this-is-you` is your GitHub username. Here you're copying the contents of the first-contributions repository on GitHub to your computer.

### Setup environment

To setup enviroments and run the tests on your local please follow resepctive READMEs of the test directories.

For example, if you want to run **HQ Smoke Tests**, please follow [steps here](https://github.com/dimagi/dimagi-qa/blob/master/HQSmokeTests/README.md) 

## First Contribution(s)

#### Follow the further steps only if you want to contribute/make changes to the scripts.

### Ensure required permissions are granted
1. [Member of organization's github ](https://github.com/orgs/dimagi/people)
2. [Added to the qa team](https://github.com/orgs/dimagi/teams/qa/members) (Not mandatory)
3. [Write access to the repo](https://github.com/dimagi/dimagi-qa/settings/access)


### Create a branch

Change to the repository directory on your computer (if you are not already there):

```
cd first-contributions
```

Now create a branch using the `git checkout` command:

```
git checkout -b your-new-branch-name
```

For example:

```
git checkout -b kt/alonzo-church
```

(The name of the branch does not need to have the word your name's initials (__kt__) in it, but it is a good practice to.)

### Make necessary changes and commit those changes

Make the necessary changes.

If you go to the project directory and execute the command `git status`, you'll see there are changes.

Add those changes to the branch you just created using the `git add` command:

```
git add <changed-file-name>
```

Now commit those changes using the `git commit` command:

```
git commit -m "Add a short message to summarize the changes"
```

### Push changes to GitHub

Push your changes using the command `git push`:

```
git push origin <add-your-branch-name>
```

replacing `<add-your-branch-name>` with the name of the branch you created earlier.

### Submit your changes for review

If you go to your repository on GitHub, you'll see a `Compare & pull request` button. Click on that button.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Now submit the pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Add a reviewer and get the PR reviewed. Once the changes are approved and merged, you will get a notification email.


### Celebrate! :tada:

