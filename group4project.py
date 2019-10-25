import pyglet
import sys
kitten_stream = open('kitten.png', 'rb')  #birinci resim
kitten = pyglet.image.load('kitten.png', file=kitten_stream)

from pyglet.image.codecs.png import PNGImageDecoder
kitten = pyglet.image.load('kitten.png', decoder=PNGImageDecoder())

image_part = kitten.get_region(x=10, y=10, width=100, height=100)
sprite1 = pyglet.sprite.Sprite(img=kitten)



kitten_stream = open('kitten.png', 'rb')  #ikinci resim
kitten = pyglet.image.load('kitten.png', file=kitten_stream)

from pyglet.image.codecs.png import PNGImageDecoder
kitten = pyglet.image.load('kitten.png', decoder=PNGImageDecoder())

image_part = kitten.get_region(x=10, y=60, width=100, height=100)
sprite2 = pyglet.sprite.Sprite(img=kitten)







window = pyglet.window.Window()
window = pyglet.window.Window(fullscreen=True)
class Timer(object):
    def __init__(self):
        self.label = pyglet.text.Label('DNA', font_size=16, 
                                       x=window.width//2, y=window.height//2,
                                       anchor_x='center', anchor_y='center')
        self.reset()

    def reset(self):
        self.time = 0
        self.running = False
        self.label.text = 'We translate DNA encoding into proteins :).\
  If you want to know yout DNA protein press esc and write it'
        
        self.label.color = (255, 0, 255, 255)

    def update(self, dt):
        if self.running:
            self.time += dt
            m, s = divmod(self.time, 60)
            self.label.text = '%02d:%02d' % (m, s)
            if m >= 5:
                self.label.color = (180, 0, 0, 255)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.SPACE:  #timer koymak için
        if timer.running:
            timer.running = False
        else:
            if timer.time > 0:
                timer.reset()
            else:
                timer.running = True
    elif symbol == pyglet.window.key.ESCAPE:
        window.close()
class ResponsiveWindow(pyglet.window.Window):
     def on_mouse_press(self,x, y, button, modifiers):
        print('You clicked the mouse!')
        print('\tYou clicked mouse button #'+str(button))
        print('\tYou clicked at coordinates: (' +str(x) + ',' + str(y) + ')')
        sys.stdout.flush()

     def on_mouse_drag(self,x, y, dx, dy, button, modifiers):
        print('You dragged the mouse!')
        print('\tYou dragged mouse button #'+str(button))
        print('\tYou clicked at coordinates: (' +str(x) + ',' + str(y) + ')')
        print('\t...and dragged the cursor ' +str(x) + ' units horizontally and ' + str(y) + ' units vertically')
        sys.stdout.flush()
def transcript():
#Returns the corresponding RNA value for a given DNA nucleotide(e.g. A --> U)
    transcription = {'A':'U', 'G':'C', 'C':'G', 'T':'A'} #DNA ---> mRNA
# Returns the corresponding amino acid for a mRNA codon
    translation = {'UUU':'Phe', 'UUC':'Phe', 'UUA':'Leu', 'UUG':'Leu', 'UCU':'Ser',
         'UCC':'Ser', 'UCA':'Ser', 'UCG':'Ser', 'UAU':'Tyr', 'UAC':'Tyr', 'AUU':'Ter',
         'AUC':'Ter', 'UGU':'Cys', 'UGC':'Cys', 'ACU':'Ter', 'UGG':'Trp', 'CUU':'Leu',
         'CUC':'Leu', 'CUA':'Leu', 'CUG':'Leu', 'CCU':'Pro', 'CCC':'Pro', 'CCA':'Pro',
         'CCG':'Pro', 'CAU':'His', 'CAC':'His', 'GUU':'Gln', 'GUC':'Gln', 'CGU':'Arg',
         'CGC':'Arg', 'CGA':'Arg', 'CGG':'Arg', 'AUU':'Ile', 'AUC':'Ile', 'AUA':'Ile',
         'AUG':'Met', 'ACU':'Thr', 'ACC':'Thr', 'ACA':'Thr', 'ACG':'Thr', 'AAU':'Asn',
         'AAC':'Asn', 'AAA':'Lys', 'AAG':'Lys', 'AGU':'Ser', 'AGC':'Ser', 'AGA':'Arg',
         'AGG':'Arg', 'GUU':'Val', 'GUC':'Val', 'GUA':'Val', 'GUG':'Val', 'GCU':'Ala',
         'GCC':'Ala', 'GCA':'Ala', 'GCG':'Ala', 'GAU':'Asp', 'GAC':'Asp', 'GAA':'Glu',
         'GAG':'Glu', 'GGU':'Gly', 'GGC':'Gly', 'GGA':'Gly','GGG':'Gly'}
         # A short sample of the DNA code for Trombosid
        
         # Try changing the below DNA string to translate a different sequence
    DNA = input("DNA'YI GİRİNİZ:")
    mRNA = ''
    protein = ''
    for base in DNA: # Pseudocode line 1 (transcription)
         mRNA += transcription[base]
    for base in range(0, len(mRNA), 3): # Pseudocode line 2 (translation)
         if base + 2 < len(mRNA): # Stop the loop before you run out of codons
             codon = mRNA[base:base + 3] # Codons are three nucleotides
         try: # See if codon is in the translation dictionary
             protein += translation[codon] + '-' # If so, add to protein chain
         except KeyError: # If it is not, stop translating (stop codon)  
             break
    print( 'DNA: ' + DNA )
    print ('mRNA: ' + mRNA)
    print ('Protein: ' + protein[:-1])



@window.event
def on_draw():
    window.clear()
    timer.label.draw()
    sprite1.draw()
    sprite2.draw()
    


timer = Timer()
responsive_window = ResponsiveWindow()
pyglet.app.run()
transcript()



# Call update 60 times a second














        
