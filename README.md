## YouTube Livestream Analysis

__________________________________________________

### Paste in a URL of a already finished livestream and see where the most laughed occured

Demo (still working on it) --> https://share.streamlit.io/maximilianfreitag/yt-livechat-analysis/main/example.py

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

__________________________________________________


### Current bugs: 
- When people are writing before the main stream started the minutes are counted as negative integers -4,-3,-2 ... this can lead to problems sometimes.    
- The web version is collecting the data for too long sometimes if you test out multiple URLs or if you re-run the code 



<br>
__________________________________________________


### To-Do list of things that I want to add as a functionality

- [ ] I want users to input a custom word e.g. spam-eggs that will be displayed in a sparate graph for the results
- [ ] I want to make the mobile version more 



<br>
__________________________________________________

<br>
<br>
<br>
<br>


## Stargazers over time

[![Stargazers over time](https://starchart.cc/MaximilianFreitag/yt-livechat-analysis.svg)](https://starchart.cc/MaximilianFreitag/yt-livechat-analysis)
