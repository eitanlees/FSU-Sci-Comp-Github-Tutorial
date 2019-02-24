# FSU Scientific Computing Github Tutorial
A repository to practice using git/github 

## Steps to contribute 

1) Fork this repository
1) Clone the forked repo to your local machine
1) Create a new remote named `upstream` that points to the primary repository (the one you forked)
1) Create a branch for the edit or feature
1) Move to the feature branch and edit away making many commits
1) Once you are done and commited all of your edits open a _pull request_ on github to merge your
branch into `master`.
1) Continue to push to the feature branch to address any issues brought up in the pull request
discussion. 
1) Hopefully the pull request eventually gets merged
1) After your feature has been merged try moving back to master and running the command

```bash
git fetch upstream
git rebase upstream/master
```

If all has gone well your feature will be show in the master branch!

This is the basis for the "GitHub Workflow". 

For more information see [Understanding the GitHub flow](https://guides.github.com/introduction/flow/).
