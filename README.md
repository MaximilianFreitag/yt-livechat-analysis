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

To-Do:

- [ ] If the user hits stop on the app the "Collecting data" symbol is still visible
- [ ] The example URL always works, other URLs are not starting to collect comments (Note to myself: Look into while chat.isalive LINE 328... maybe you have to start the video in the background first)
- [ ] After 10 minutes runtime streamlit thinks the app isn't working anymore and stops the runtime.
- [ ] Messages that were posted over one hour before the stream started are not properly handled by the get_minutes() function. E.g. the timestamp -2:12:42 will not be turned into -212 (desired output) by the function... -59:42 --> -59 .... -1:44:04 --> ??? doesn't work and it should return -144. As a result, the plot function ignores those values.




<br>
__________________________________________________

<br>
<br>

### To-Do list: (Improvements and functionality)

- [x] I want to add additional text boxes for the user to input custom words e.g. spam ... eggs ...that will be displayed in a sparate graph for the results. So the user sees "Oh, the word spam was mentioned 42 times in minute 33 and eggs was mentioned 7 times in minute 55".
- [ ] I want to add spacing for the mobile version. Currently just writing something like st.write('  ') or using line breaks like br 'doesn't work for mobile
- [x] Display the most current 5 collected messages while the data is being collected (Note to myself: Use streamlit's st.empty for collapsing)
- [ ] Make the theme of the app white, currently it depends on the users settings if the app appears in light or dark mode. Adding a .config file changes that
- [ ] Getting rid of the timestamp when the user accidentally pastes in a URL + timestamp... e.g. URL ends with &t=2195s
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
