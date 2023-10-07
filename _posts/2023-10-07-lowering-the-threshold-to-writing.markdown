---
layout: post
title: "Lowering the threshold to writing"
categories: [Automation, Jekyll, VS Code]
---



As I sat down to write down some thoughts on the automation of taskst, perfectly summarised by Randal Mundoe in xkcd 1319,
I first had to look up the correct formatting for a post using Jekyll.
Which reminded me that I have to manually enter information in two places;
title and date should be both in the filename and in the file for the individual post.
This is not only tedious, but prone to errors.
Ergo this should be automated.
As I have recently started using VS Code, the first place I looked was in the extension marketplace and there were a few options there but none that felt right for what I want out of such a tool --
one tool [*jekyll-post* by **Rohan Garg**](https: //marketplace.visualstudio.com/items?itemName=rohgarg.jekyll-post)
relies on a VS Code template.
Writing a template seems simple enough, so I might as well write my own using the built in template functionality in VS Code. Then all I need to do is create a simple Python script to be triggered by pre-commit to add the correct timestamp and title!

Should be simple enough, and anything that can be automated should be automated. It is not like anyone ever spent more time on automating a task than just performing the task.

![['Automating' comes from the roots 'auto-' meaning 'self-', and 'mating', meaning 'screwing'](https: //xkcd.com/1319/)](https://imgs.xkcd.com/comics/automation.png)
- date
  - hyphen
  - lowercase title with whitespaces replaced by hyphens
3. A really tiny Python file that reformats all posts without dates in their filenames, in part so that I can quickly run the formatter without having to run pre-commit in part because I want to be prepared to reformat all posts in the future should the need arise.
4. The .pre-commit-config.yaml where I entered the local script as a pre-commit step.

## The snippet
```json
(
	"New Jekyll Post": (
"prefix": ["post"],
"body": "---
date: 2023-10-07 14:44:48 +0200
---


\n\n",
		"description": "Create new jekyll Post",
	)
)
```


I replaced the curly brackets with paranthesis because my local preview environment is unable to render them, and suspect that it will make the post unreadable. A quite nice thing with this setup is that it lets me jump between setting a title and the categories if I edit it directly after the snippet is activated.

True to form, I have now spent a lot more time on this simple setup than simply writing. But if it works as intended, it will lower the thershold to start writing and to posting that it should repay itself soon.
