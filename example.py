import streamlit as st
import pandas as pd
import numpy as np
import pytchat as pytchat
import matplotlib.pyplot as plt
#import plotly
import plotly.graph_objects as go
from PIL import Image
import time as time



#Favicon and Header
st.set_page_config(
        page_title='YouTube Livechat Analyse                 ',
        page_icon="📊"
        )



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 






#START VALUES
authors = []
all_authors = []
messages = []
messages_lower = []
supporters = []
timestamps = []
laugh = []
mods = []


wort1 = []
wort2 = []
wort3 = []
five_messages = []



liveChat = None



col1, col2, col3, col4, col5 = st.columns([1,1,5,1,1])


#These columns ensure that the app is centered and compatible on mobile
with col1:
        st.write("")

with col2:
        st.write("")        

with col4:
        st.write("")  

with col5:
        st.write("")  

        
        
        

with col3:
    st.title('Youtube Livestream Analyse')

    st.write('Gebe eine URL eines bereits beendeten YouTube livestreams ein und vergewissere dich, dass die Wiedergabe des chats aktiviert wurde. ')
        
    image = Image.open('123.jpg')
    st.image(image, caption='Beispiel einer Wiedergabe des chats aus einem stream')
    
    st.write('Die Analyse funktioniert NICHT bei gerade laufenden livestreams! ')
    st.write('Hier ist eine Beispiel URL eines streams der 125 Minuten ging. Copy/Paste den folgenden Link, wenn du einfach nur diese app austesten möchtest')
    
    st.code('https://youtu.be/WPvWiTeZ858')
    
    st.write('Wenn du deine eigene URL eingibst und auf "Start" drückst, wird die Analyse gestartet. Der stream muss einmal komplett durchlaufen. Falls etwas schief läuft einfach die Seite aktualisieren und nochmal versuchen.')
    
    


    
    #USER CAN ENTER CUSTOM WORDS

    with st.expander("Möchtest du die Häufigkeit von spezifischen Wörtern analysieren?"):
        #create a text input
        st.write('Wenn du diesen Schritt auslassen möchtest, lasse die Felder leer. Beachte: Groß-und Kleinschreibung sind egal, aber looooooool ist nicht dasselbe wie lol.')
        
        wort_a = st.text_input('Wort 1')
        wort_a = wort_a.lower()
        
        #if the user entered no word, then pass
        if wort_a == '':
            #code appends a really unlikely word to the list
            wort1.append('helloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworld')

        wort_b = st.text_input('Wort 2')
        wort_b = wort_b.lower()

        if wort_b == '':
            wort2.append('helloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworld')

        wort_c = st.text_input('Wort 3')
        wort_c = wort_c.lower()

        if wort_c == '':
            wort3.append('helloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworld')







    st.markdown("***")
    
    #text box input + video url
    url = st.text_input(" ", placeholder="https://www.youtube.com/watch?v=QH2-TGUlwu4")

    #if url is empty display enter a url
    if url == '':
        st.write('Gebe die URL hier ein und drücke "Start"')
        video_id = 'QH2-TGUlwu4'

    #if the url does not start with https://www.youtube.com/watch?v=
    if url.startswith('https://www.youtube.com/watch?v='):
        video_id = url.split('=')[1] 
        #st.write(video_id)

    if url.startswith('https://youtu.be'):
        video_id = url.split('be/')[1] 
        #st.write(video_id)
    
   
    




#Diese Funktion wandelt alle timestamps (25:38) zu einer einzelnen Minute um (25)
#Also aus 56:33 wird dann 56
def get_minutes(timestamps):
    minutes_list = []
    for minute in timestamps:
        #if minute is 4 characters long
        if len(minute) == 4 or len(minute) == 5:
            minutes_list.append(minute.split(':')[0])

        elif len(minute) == 7:
            #input: 1:11:01
            #output: 111
            
            minutes_list.append(minute.split(':')[0] + minute.split(':')[1])
            
    return minutes_list





chat = pytchat.create(video_id, interruptable=False)



def plot():
    st.markdown("***")    
    st.write('Hier ist das Ergebnis:')
    
    st.write('Wie viele individuelle user kommentierten?')
    st.write(len(authors))

    st.markdown("***")
    st.write('Gesamtzahl aller Nachrichten')
    st.write(len(messages))
        
    st.markdown("***")
    #output the string that appears most often in all_authors
    st.write('User der am meisten kommentiert hat')
    st.write(max(all_authors, key=all_authors.count))
    st.markdown("***")

    st.write('Anwesende mods')
    #if the mod list is empty
    if len(mods) == 0:
        st.write('Es waren keine mods anwesend')
    else:
        #only output unique values
        st.write(list(set(mods)))
        
    st.markdown("***")

    st.write('Verlauf der Anzahl der Nachrichten pro Minute:')
    occurences = get_minutes(timestamps)
    #plot the occurences with streamlit
    #st.write(occurences)
    st.plotly_chart(create_plotly_figure(occurences))
    #st.write(occurences)

    st.markdown("***")

    st.write('In welcher Minute lachte der YouTube chat am meisten? (haha, lol, lel, emojis, xD, ...)')
    laugh_occurences = get_minutes(laugh)
    
    #if laugh_occurences is empty
    if len(laugh_occurences) == 0:
        st.write('Es wurde im chat nicht gelacht.')
    elif len(laugh_occurences) > 0:
        st.plotly_chart(create_plotly_figure(laugh_occurences))






    def wort_eins():
        
        if 'helloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworld' in wort1:
            st.write(' ')
            pass

        elif 'helloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworld' not in wort1 and len(wort1) == 0:
            st.write(f' ... {wort_a} ...wurde von keinem user geschrieben')
            pass

        else:
            st.write(f' Häufigkeit von ... {wort_a} ... im zeitlichen Verlauf.')
            wort1_occurences = get_minutes(wort1)
            st.plotly_chart(create_plotly_figure(wort1_occurences))
            st.markdown("***")
    
    wort_eins()
  



    def wort_zwei():
        
        if 'helloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworld' in wort2:
            st.write(' ')
            pass

        elif 'helloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworld' not in wort2 and len(wort2) == 0:
            st.write(f' ... {wort_b} ...wurde von keinem user geschrieben')
            pass

        else:
            st.write(f' Häufigkeit von ... {wort_b} ... im zeitlichen Verlauf.')
            wort2_occurences = get_minutes(wort2)
            st.plotly_chart(create_plotly_figure(wort2_occurences))
            st.markdown("***")
            

    wort_zwei()





    def wort_drei():
        
        if 'helloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworld' in wort3:
            st.write(' ')
            pass

        elif 'helloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworldhelloworld' not in wort3 and len(wort3) == 0:
            st.write(f' ... {wort_c} ...wurde von keinem user geschrieben')
            pass        

        else:
            st.write(f' Häufigkeit von ... {wort_c} ... im zeitlichen Verlauf.')
            wort3_occurences = get_minutes(wort3)
            st.plotly_chart(create_plotly_figure(wort3_occurences))
            st.markdown("***")

    wort_drei()







def create_plotly_figure(occurences):
    #create a figure
    fig = go.Figure()

    #add a histogram
    fig.add_trace(go.Histogram(x=occurences))

    #add some layout features
    fig.update_layout(
        #title_text='Minutes of the day',
        xaxis_title_text='In welcher Minute (120 bedeutet 1h 20min)',
        yaxis_title_text='Anzahl der Nachrichten'
    )

    return fig    
    
    
    





#Die Hauptfunktion zum sammeln der Daten
def main():

  global chat
  _emp = st.empty()
  
  #Adding a GIF?
  #st.image('https://media.giphy.com/media/l46Cy1rHbQ92uuLXa/giphy.gif')
  st.write('Wenn keine Nachrichten vom chat angezeigt werden, ist etwas schief gelaufen. :/')
        

  while chat.is_alive():
        
        
        #display a gif
        #data_load_state = st.text('Please wait...')
                
        for c in chat.get().sync_items():


            #FILTER MESSAGES
            if c.message.startswith('!') or c.author.name == 'Streamlabs':
                pass
            
            
            #APPEND AND OUTPUT FILTERED MESSAGES 
            else:
##########################################################################################################################################                
                
                messages.append(c.message)
                lowercase = c.message.lower()
                messages_lower.append(lowercase)

                five_messages.append(c.message)

                #st.write(f" {c.author.name} // {c.message} // {c.elapsedTime} // {c.amountString}")
                
                
                #display only the last 5 messages and use st.empty() to hide the rest
                for x in five_messages:
                    pos = five_messages.index(x)
                    d = five_messages[pos:pos+5]
                    if pos < 10:
                        #time.sleep(0.05)
                        _emp.code(f" {c.author.name} // {c.message} // {c.elapsedTime} // {c.amountString}")




##########################################################################################################################################

                 #Alle Timestamps
                #TIMESTAMPS 0:00
                #time_elapsed = format_time(time.time() - start_time)
                timestamps.append(c.elapsedTime)
            
                all_authors.append(c.author.name)
        

                #UNIQUE AUTHORS
                if c.author.name not in authors:
                    authors.append(c.author.name)
            
                if c.author.isChatModerator == True:
                    mods.append(c.author.name)
                


                #EXTRACT LAUGHS
                if "haha" in c.message or ":rolling_on_the_floor_laughing:" in c.message or "lel" in c.message or "LeL" in c.message or "LEL" in c.message or "Haha" in c.message or ":grinning_squinting_face:" in c.message or ":face_with_tears_of_joy:" in c.message or "lol" in c.message or "LOL" in c.message or "HAHA" in c.message or "XD" in c.message or "xD" in c.message or "lol" in c.message:
                    laugh.append(c.elapsedTime)


                #EXTRACT CUSTOM WORDS
                if wort_a in lowercase:
                    wort1.append(c.elapsedTime)

                if wort_b in lowercase:
                    wort2.append(c.elapsedTime)

                if wort_c in lowercase:
                    wort3.append(c.elapsedTime)

                

               


  st.write('Fertig')
  
  

if __name__ == "__main__":
    with col3:
        if st.button('Start', key="1"):
            with st.spinner('Daten werden gesammelt...'):
                main()
                #wait 1 second
                time.sleep(1)
                plot()

                st.success('Fertig!') 


                #set values from list back to 0
                messages.clear()
                timestamps.clear()
                all_authors.clear()
                wort1.clear()
                wort2.clear()
                wort3.clear()
                laugh.clear()
                authors.clear()
                mods.clear()
                supporters.clear()
                video_id = ''










footer="""<style>
a:link , a:visited{
color: red;
background-color: transparent;
text-decoration: underline;
}
a:hover,  a:active {
color: LightBlue;
background-color: transparent;
text-decoration: underline;
}
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: transparent;
color: grey;
text-align: center;
}
</style>
<div class="footer">
<p>Entwickelt mit ❤️  von <a style='display: inline-block;' href="https://www.instagram.com/max_mnemo/" target="_blank">Max Mnemo </a> + <a style='display: block-inline; text-align: center;' href="https://www.github.com/MaximilianFreitag/yt-livechat-analysis" target="_blank">Github </a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
