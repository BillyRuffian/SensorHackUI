from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

class Crossing( BoxLayout ):
  wait_cross_label = StringProperty()
  wait_cross_color = ListProperty()

  IDLE = (0.5, 0.5, 0.5, 1)
  WAIT = (1, .8, 0, 1)
  CROSS = (0, 1, 0, 1)
  STOP = (1, 0, 0, 1)

  def __init__( self, **kwargs ):
    super(Crossing, self).__init__(**kwargs)
    self.wait_cross_label = '\uF256'
    self.wait_cross_color = self.IDLE

  def button_pressed( self ):
    self.wait_cross_color = self.WAIT
    self.wait_cross_label = '\uF183'
    Clock.schedule_once( self.cross, 1 )
    self.ids.cross_button.disabled = True
    print( "Button pressed" )

  def cross( ref, dt ):
    ref.wait_cross_label = '\uf554'
    ref.wait_cross_color = ref.CROSS
    Clock.schedule_once( ref.stop, 1 )
  
  def stop( ref, dt ):
    ref.wait_cross_label = '\uf70c'
    ref.wait_cross_color = ref.STOP


class CrossingApp( App ):
  def build( self ):
    return Crossing()

if __name__ == '__main__':
  CrossingApp().run()