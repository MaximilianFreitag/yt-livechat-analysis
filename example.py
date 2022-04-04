import streamlit as st
import pandas as pd
import numpy as np
import pytchat as pytchat
import matplotlib.pyplot as plt
#import plotly
import plotly.graph_objects as go
from PIL import Image
import time as time
import operator
import urllib
from wordcloud import WordCloud
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
from collections import Counter



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


#Necassary for the line 484 so that streamlit doesn't show the message... pass arguments
st.set_option('deprecation.showPyplotGlobalUse', False)



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
    st.write('Hier ist eine Beispiel URL eines Streams der 125 Minuten ging. Copy/Paste den folgenden Link, wenn du einfach nur diese app austesten möchtest')
    
    st.code('https://youtu.be/WPvWiTeZ858')
    
    st.write('Wenn du deine eigene URL eingibst und auf "Start" drückst, wird die Analyse gestartet. Der stream muss einmal komplett durchlaufen. Falls überhaupt nichts klappt, dann klicke unten auf mein Github Profil. Da habe ich eine Google Colab Datei, die immer funktioniert.')
    
    


    
    #USER CAN ENTER CUSTOM WORDS

    with st.expander("Möchtest du die Häufigkeit von spezifischen Wörtern analysieren?"):
        #create a text input
        st.write('Wenn du diesen Schritt auslassen möchtest, lasse die Felder leer.')
        st.write('Für emojis, trage den emojipedia.org shortcode ein, NICHT das Emoji selbst... :heart: wird zu :red_heart: ...Beachte: Groß-und Kleinschreibung sind egal, aber Blumeeeee ist nicht dasselbe wie Blume.')
        st.write('Satzzeichen funktionieren natürlich auch. Probiere es mal aus mit ?, um zu gucken, wo Fragen gestellt wurden und :red_heart: um zu sehen, ab welcher Minute Herzen verteilt wurden.')
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
        
    if '&t=' in url:
        video_id = url.split('&t=')[0].split('=')[1]    
    
    if '?t=' in url:
        video_id = url.split('?t=')[0].split('/')[-1]  
        
        
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
    #st.write('User der am meisten kommentiert hat')
    #st.write(max(all_authors, key=all_authors.count))
        
    st.write('Top 3 User die am meisten kommentiert haben')
    st.write(max(all_authors, key=all_authors.count))
    
    #output the string that appears the second most often in all_authors
    st.write(all_authors[all_authors.index(max(all_authors, key=all_authors.count)) + 1])

    #output the string that appears the third most often in all_authors
    st.write(all_authors[all_authors.index(max(all_authors, key=all_authors.count)) + 2])
     
        
    st.markdown("***")


    st.write('Anwesende mods')
    #if the mod list is empty
    if len(mods) == 0:
        st.write('Es waren keine mods anwesend')
    else:
        #only output unique values
        unique_mods = list(set(mods))
        for i in unique_mods:
            st.write(i)
        
    st.markdown("***")
    st.markdown("<h6 style='text-align: center; color: black;'>Verlauf der Anzahl der Nachrichten pro Minute:</h6>", unsafe_allow_html=True)
    
    occurences = get_minutes(timestamps)
    #plot the occurences with streamlit
    #st.write(occurences)
    st.plotly_chart(create_plotly_figure(occurences))
    #st.write(occurences)

    st.markdown("***")

    st.markdown("<h6 style='text-align: center; color: black;'>In welcher Minute lachte der YouTube chat am meisten? (haha, lol, lel, emojis, xD, ...)</h6>", unsafe_allow_html=True)
    
    laugh_occurences = get_minutes(laugh)
    
    #if laugh_occurences is empty
    if len(laugh_occurences) == 0:
        st.write('Es wurde im chat nicht gelacht. :/')
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
  st.write('Wenn keine Nachrichten vom chat angezeigt werden, ist etwas schief gelaufen. 😑')
        

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
  

















#Creating a WORDCLOUD
#########################
def make_wordcloud(messages):

   

    #FETCH german stop words from a github repo
    url = 'https://raw.githubusercontent.com/solariz/german_stopwords/master/german_stopwords_plain.txt'
    with urllib.request.urlopen(url) as response:
        german_stopwords = response.read().decode('utf-8').splitlines()


    #removing the first 10 words from the list
    german_stopwords = german_stopwords[9:]
    add_words = ['und', 'in', 'statt', 'mal']
    german_stopwords = german_stopwords + add_words

    wordcloud_messages = [x.lower() for x in messages]
    #make each word separate in a list so that there are no sentences
    wordcloud_messages2 = [x.split() for x in wordcloud_messages]
    #make one big list
    wordcloud_messages3 = [item for sublist in wordcloud_messages2 for item in sublist]
    
    #remove stopwords
    wordcloud_messages4 = [x for x in wordcloud_messages3 if x not in german_stopwords]
    
    
    #make a wordcloud from the list wordcloud_messages4
    wordcloud = WordCloud(width=800, height=800, max_font_size=200, background_color='white').generate(' '.join(wordcloud_messages4))
    fig, ax = plt.subplots()
    plt.figure(figsize=(10, 10), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    st.pyplot(fig=None, clear_figure=None)





def natural_language_processing(messages):
    
    
    


    model_name = 'oliverguhr/german-sentiment-bert'


    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    X_train_german= messages
    batch = tokenizer(X_train_german, padding=True, truncation=True, max_length = 512, return_tensors='pt')
    batch = torch.tensor(batch['input_ids'])
    #print(batch)



    with torch.no_grad():
        outputs = model(batch)
        label_ids = torch.argmax(outputs.logits, dim=1)
        #print(label_ids)
        labels = [model.config.id2label[label_id] for label_id in label_ids.tolist()]
        print(labels)


    #Count the labels
    count = Counter(labels)

    plt.bar(count.keys(), count.values(), width=0.5, color='blue')
    #make the graph look nicer
    plt.title('Die Labels der Ki')
    plt.ylabel('Anzahl der Vorkommnisse')

   
    #make the text bigger
    st.pyplot(fig=None, clear_figure=None)






def beschreibung_wordcloud():
    st.markdown("***")
    st.write('  ')
    #make a st.markdown heading h2
    st.markdown("<h3 style='text-align: center; color: black;'>Wortwolke</h3>", unsafe_allow_html=True)
    st.write('Welche Wörter kamen häufig vor im Chat? (Ohne Stoppwörter, aber mit emojis z.B. red_heart) ')
    #make a drop down menu
    
    with st.expander("Erklärung: Was sind Wortwolken/Stoppwörter?"):
        
        st.write('  ')
        st.write('Da ich mit meinem Code jeden einzelnen Satz im chat gesammelt habe, kann man aus diesen Daten, die am häufigsten vorkommenden Wörter entnehmen.')
        st.write('Um dies zu veranschaulichen kann man als visuelle Hilfe eine sogenannte Wortwolke bilden.')
        st.write('Bei dieser Wortwolke habe ich Stoppwörter so gut es geht entfernt. Stoppwörter sind nichts anderes als die häufigsten Wörter innerhalb einer Sprache.')
        st.write('Z.B. Un/bestimmte Artikel (der, die, das, ein, eine) oder auch Präpositionen (auf, über, unter,...)')
        st.write('Aus diesen Wörtern kann man schwer was ableiten und sie behindern eher die Analyse. ')
    
    st.write('  ')









def beschreibung_sentiment():
    st.markdown("***")
    st.write('  ')
    #make a st.markdown heading h2
    st.markdown("<h3 style='text-align: center; color: black;'>Computerlinguistik</h3>", unsafe_allow_html=True)
    st.write('Wie war die allgemeine Stimmung im Stream? 😊 😡 ')
    #make a drop down menu
    
    with st.expander("Erklärung: Was hat es mit der Computerlinguistik auf sich und wie funktioniert mein Code?"):
        #create a text input
        st.write('Ich habe die Bibliothek Huggingface verwendet, die in der Computerlinguistik dazu verwendet wird, um Stimmungen von Sätzen zu bestimmen.')
        st.write('Hierfür habe ich eine Ki verwendet, die auf deutsche Sätze von einem Programmierer trainiert wurde. Das heißt, jemand hat sich die Mühe gemacht tausende Sätze mit schlechten und guten Stimmungen zu sammeln und somit die Ki zu trainieren.')
        st.write('Sätze wie "Er ist so ein Idiot" erhalten von der Ki z.B. einen Sentiment-Score von 0.98, was bedeutet, dass die KI zu 98 Prozent sicher ist, dass dieser Satz eine negative Stimmung hat.')
        st.write('Sätze, bei denen die KI einen bestimmten Sentiment-Score nicht übersteigt, z.B. der Satz "Die Mauer ist grün" ... (0,15) ... werden als neutral gelabelt')
        st.write('Das Gleiche gilt für positive Stimmungen. Positive Sätze wie "Ich liebe Waffeln" ... (0,97) ... erhalten ebenfalls eine Stimmungsbewertung. Bei den Waffel-satz ist sich die KI zu 97 Prozent sicher, dass der Satz positiv gemeint war')
        st.write('Wie man sich vorstellen kann, ist es für KIs schwer, sarkastische, ironische Sätze zu erkennen. Z.B. "Ich bin so froh, dass eine neue Pandemie auf uns zukommt." ... trotzdem kann man aber ein insgesamt gutes Ergebnis erzielen.')
        











if __name__ == "__main__":
    with col3:
        if st.button('Start', key="1"):
            with st.spinner('Daten werden gesammelt...'):
                main()
                #wait 1 second
                time.sleep(1)
                plot()

                #wordcloud
                beschreibung_wordcloud()
                make_wordcloud(messages)  

                #add some whitespace
                st.write(' ')
                st.write(' ')

                #natural language analysis
                beschreibung_sentiment()
                st.write(' ')
                natural_language_processing(messages)
                st.write(f'Es wurden ...{len(messages)}... Sätze von der Ki analysiert und gelabelt.')


                st.write(' ')
                st.write(' ')
                st.write(' ')
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
<p>Entwickelt mit ❤️  von <a style='display: inline-block;' href="https://www.instagram.com/max_mnemo/" target="_blank">Max Mnemo </a> // <a style='display: block-inline; text-align: center;' href="https://www.github.com/MaximilianFreitag/yt-livechat-analysis" target="_blank">Github </a> // <a style='display: block-inline; text-align: center;' href="https://mnemo.uk/contact/" target="_blank">Contact </a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
