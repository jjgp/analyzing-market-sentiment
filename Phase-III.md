<p align = "center" draggable=”false” ><img src="https://user-images.githubusercontent.com/37101144/161836199-fdb0219d-0361-4988-bf26-48b0fad160a3.png"
     width="200px"
     height="auto"/>
</p>



# <h1 align="center" id="heading">Phase III - Deploying an ML App on Hugging Face🤗 Spaces</h1>



## ☑️ Objectives
At the end of this session, you will have a brief understanding of how to:
- [ ] Deploy an ML App on Hugging Face🤗 Spaces


## Tasks
There are two tasks for this phase:
1. Create a Hugging Face🤗 Space
2. Clone your new Space and add your Streamlit app to your Hugging Face🤗 Space

Before we get started, make sure you've created an account on Hugging Face🤗, and that you've verified your email address!

<details>
<summary>Task 1: Create a Hugging Face🤗 Space</summary>
<br>

1. Navigate to Hugging Face🤗's Spaces [page](https://huggingface.co/spaces) and click the `Create New Space` button!
2. Give your Space a cool name.
3. Make sure to select Streamlit as your Space SDK
4. Ensure the Space is public, and click `Create space`

![image](https://i.imgur.com/ofzBqfb.png)

5. You're ready to move to the next step!
</details>

<details>
<summary>Task 2: Cloning your Space and Adding Your App</summary>
<br>

1. We'll want to navigate outside of any existing repository directory and use the command, after it runs we'll want to CD into the created directory:

```console
git clone https://huggingface.co/spaces/<YOUR HUGGINGFACE ACCT.>/<YOUR SPACE NAME>
```

```console
cd <YOUR SPACE NAME>
```

2. We'll want to add our working Streamlit `.py` file, as well as the `images` folder and the `sentiment_data.csv` from the previous phase of Week 1 to this repository. You can do it through the graphical user interface, or you can use the provided command to copy the contents of the folder your Streamlit app resides in. (The `-a` tag here lets us recursively copy the *contents* of the directory we're pointing at. We want to do this becasue we want our streamlit `.py` file to be at the top level, not tucked away in a directory)

```console
cp -a ../Path/To/Dir/Containing/Streamlit/App/. .
```

3. We'll want to rename our streamlit app to `app.py`. We can use the following command to achieve this:

```console
mv your_streamlit_app.py app.py
```

4. We'll want to make sure we have the appropriate `requirements.txt` so that our Hugging Face🤗 space knows the correct requirements to install. To do this, we'll use an awesome tool called `pipreqs` (more info [here](https://pypi.org/project/pipreqs/)) First things first, let's grab `pipreqs` from `pip` (make sure your MLops Short Course conda environment is activated!):

```console
pip install pipreqs
```

5. Now we can run a simple command to generate a `requirements.txt` file:

```console
pipreqs .
```

6. Let's verify that our file structure looks as follows by using the `tree` command:

![image](https://i.imgur.com/3rL9sxu.png)

7. Once you've verified that you have the appropriate file structure: Let's push this all to the space! We'll use the classic:

```console
git add .
```
```console
git commit -m "ADD A MESSAGE HERE"
```

```console
git push
```

8. At this point, you will be prompted to enter your Hugging Face🤗 username and password. Enter them to continue. You should see the push complete successfully.

9. Now we can navigate to your Space at the url: huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME, and we should see the following:

![image](https://i.imgur.com/wxiTz2V.png)

10. Let it build. (you can check the progress by click on the `See logs` button next to where it says "* Building")

11. Once it's done - refresh - and you should see your Streamlit app working, and deployed on Hugging Face🤗 Spaces!

</details>

<details>
<summary> Optional: Configuring your Space </summary>
<br>

1. Configuration is done through editing a YAML block at the top of the **README.md** file at the root of the repository.

2. You can check out configuration options [here](https://huggingface.co/docs/hub/spaces-config-reference)

3. Try editing your Space's title, and emoji ! You can edit the YAML block through the web interface, or locally - and push the changes using the same instructions we followed before.

</details>

Congrats! 🎉🎉🎉

You've just successfully deployed your ML app to Hugging Face🤗 Spaces! Spaces is a powerful tool that can do a whole lot, and is a great way to provide access to your models, and apps!

BONUS: See if you can count how many 🤗 were used in the making of this tutorial!

## Background
Please review the weekly narrative [here](https://www.notion.so/Analyzing-Market-Sentiment-Phase-I-II-and-II-End-to-End-MLOps-with-Open-Source-Tools-dc4b846108b44f6bb2962d550368560c)

## References
[Hugging Face Space Configuration Options](https://huggingface.co/docs/hub/spaces-config-reference)\
[Hugging Face🤗 Spaces Documentation](https://huggingface.co/docs/hub/spaces)\
[Info. on Spaces from Hugging Face🤗](https://huggingface.co/spaces/launch)\
[Advanced Space Management Through GitHub Actions](https://huggingface.co/docs/hub/spaces-github-actions)\
[FourthBrain Tesla Sentiment Analyzer](https://huggingface.co/spaces/FourthBrain/TSLA-Market-Sentiment-Analyzer)
