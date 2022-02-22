## YouTube Livestream Analysis

__________________________________________________

### Paste in a URL of a already finished livestream and see where the most laughed occured

Demo --> https://share.streamlit.io/maximilianfreitag/yt-livechat-analysis/main/example.py

Google Colab File, same code but a "ugly" UI (Works all the time) --> https://colab.research.google.com/drive/1lUkc92nJoa-VO8-1whUx5LT_XyD_pzrW?usp=sharing 

<br>

![789789789789](https://user-images.githubusercontent.com/46624616/153844790-f9c62c62-760e-4321-826f-2f1747debe03.jpg)

__________________________________________________


<!-- GETTING STARTED -->
## Running the app locally on your computer


1. Git clone the repository to your Desktop and install streamlit and the necessary modules pytchat and plotly via pip
   ```sh
   git clone https://github.com/MaximilianFreitag/yt-livechat-analysis.git
   pip install streamlit
   pip install pytchat
   pip install plotly
   ```

2. cd into the folder "yt-livestream" on your desktop
   ```sh
   cd yt-livestream
   ```
   
3. Run the file "example.py" in the folder with:
   ```sh
   streamlit run example.py
   ```

4. The file now runs locally on your machine

<br>

__________________________________________________

<br>

### Current bugs: 🐞

- The web version isn't properly working. Running the code locally or in my google colab file works just fine. The only link that works on the web version is the one that I provided. Maybe pytchat has a module that only works on your local machine. Maybe I forgot to erase a variable within my code so that it only works for one specific URL   



<br>
__________________________________________________

<br>
<br>

### To-Do list: (Things that I want to add as a functionality)

- [x] I want to add additional text boxes for the user to input custom words e.g. spam ... eggs ...that will be displayed in a sparate graph for the results. So the user sees "Oh, the word spam was mentioned 42 times in minute 33 and eggs was mentioned 7 times in minute 55".
- [ ] I want to add spacing for the mobile version. Currently just writing something like st.write('  ') or using line breaks like br 'doesn't work for mobile
- [ ] Add a giphy GIF for the loading state or something visual for the loading state, maybe the most current 5 collected messages
- [ ] Make the theme of the app white, currently it depends on the users settings if the app appears in light or dark mode. Adding a .config file changes that
- [ ] Getting rid of the timestamp when the user pastes in a URL + timestamp ... URL + timestamp (youtube.com/watch?v=e7EVbT0W9uU&t=2195s) ... (ends with &t=2195s)
- [ ] Add a hyperlink to each graph, e.g. This is where the most laughs occured --> https:// ....timestamp


<br>
<br>

__________________________________________________

<br>
<br>
<br>
<br>


## Stargazers over time

[![Stargazers over time](https://starchart.cc/MaximilianFreitag/yt-livechat-analysis.svg)](https://starchart.cc/MaximilianFreitag/yt-livechat-analysis)
