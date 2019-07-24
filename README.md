# tugboat
A tiny git repository puller using GitHub webhooks

## Motivation

I made this because I didn't want to run an entire jenkins instance or give someone access to my machine. I'm pretty proud of it as it is the first non-academic thing I wrote to solve a problem for myself. 

## Configuration

First thing you need to do, is set up webhooks for your GitHub or GitLab repo, and point them to the endpoint running tugboat. Then, just put your repo names and paths into the repo_names and repo_paths arrays. Next, just do a push and voila!

## Contributions

If you want to help clean my code up, I would greatly appreciate it
