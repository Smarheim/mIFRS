import math
import PySimpleGUI as sg

SIZE_X = 200
SIZE_Y = 100
NUMBER_MARKER_FREQUENCY = 25

graph = sg.Graph(canvas_size=(350, 250),
          graph_bottom_left=(-(SIZE_X+5), -(SIZE_Y+5)),
          graph_top_right=(SIZE_X+5, SIZE_Y+5),
          background_color='white',
          key='graph')

col = [[sg.Text('Pre-configured test programs, press to run program:')],
       [sg.Button('Program 1', button_color=('white', 'grey'), size=(10, 1)), sg.Text('Preset speed: "---cm/s" , preset duration: "---s"')],
       [sg.Button('Program 2', button_color=('white', 'grey'), size=(10, 1)), sg.Text('Preset speed: "---cm/s" , preset duration: "---s"')],
       [sg.Button('Program 3', button_color=('white', 'grey'), size=(10, 1)), sg.Text('Preset speed: "---cm/s" , preset duration: "---s"')],
       [sg.Button('Program 4', button_color=('white', 'grey'), size=(10, 1)), sg.Text('Preset speed: "---cm/s" , preset duration: "---s"')],
       [sg.Button('Program 5', button_color=('white', 'grey'), size=(10, 1)), sg.Text('Preset speed: "---cm/s" , preset duration: "---s"')]
       ]


layout = [[sg.Text('Start and Stop button for the motor, accompanied with an input field for RPM')],
        [sg.Button('Start', button_color=('white', 'springgreen4'), size=(5, 2)),
           sg.Button('Stop', button_color=('white', 'firebrick3'), size=(5, 2)), sg.Text('Input desired RPM:'), sg.Input(key ='-IN-', size=(15, 5))],
          [sg.Text('Graph displaying motor rpm/time, from encoder data'), sg.Text('                                     Graph displaying pump filling/flushing/emptying', justification='r')],
        [sg.Graph(canvas_size=(350, 250), graph_bottom_left=(-105, -105), graph_top_right=(105, 105),
                    background_color='white', key='graph', tooltip='This is a cool graph!'), sg.Graph(canvas_size=(350, 250), graph_bottom_left=(-105,-105), graph_top_right=(105,105), background_color='white', key='graph1', tooltip='This is a cool graph!')],
          [sg.Text('Change PWM motor:'), sg.Slider(range=(0, 100), orientation='h', size=(33, 30), default_value=30), sg.Text('Change PWM pumps:'), sg.Slider(range=(0, 100), orientation='h', size=(33, 30), default_value=85)],
          [sg.Text('Graph displaying flow velocity, measured by pendulum angle')],
          [sg.Graph(canvas_size=(350, 250), graph_bottom_left=(-105, -105), graph_top_right=(105, 105),
                    background_color='white', key='graph2', tooltip='This is a cool graph!'), sg.Column(col)],
          [sg.Text('Pendulum color tracking control:'), sg.Text('Hue value:'), sg.Input(size=(5, 5)), sg.Text('Saturation value:'), sg.Input(size=(5, 5)), sg.Text('Pixel-feed value:'), sg.Input(size=(5, 5))],
          [sg.Text('To exit the program:', justification='r' ), sg.Exit()],
          ]

window = sg.Window('HMI for Intermittent Flow Respirometry System', layout, grab_anywhere=False, finalize=True)

graph = window['graph']
graph1 = window['graph1']
graph2 = window['graph2']

sg.change_look_and_feel('Dark')

# Draw axis
graph.DrawLine((-100,0), (100,0))
graph.DrawLine((0,-100), (0,100))

for x in range(-100, 101, 20):
    graph.DrawLine((x,-3), (x,3))
    if x != 0:
        graph.DrawText( x, (x,-10), color='green')

for y in range(-100, 101, 20):
    graph.DrawLine((-3,y), (3,y))
    if y != 0:
        graph.DrawText( y, (-10,y), color='blue')

# Draw Graph
for x in range(-100,100):
    y = math.sin(x/20)*50
    graph.DrawCircle((x,y), 1, line_color='blue', fill_color='red')


# Draw axis    
graph1.DrawLine((-100,0), (100,0))
graph1.DrawLine((0,-100), (0,100))

for x in range(-100, 101, 20):
    graph1.DrawLine((x,-3), (x,3))
    if x != 0:
        graph1.DrawText( x, (x,-10), color='green')

for y in range(-100, 101, 20):
    graph1.DrawLine((-3,y), (3,y))
    if y != 0:
        graph1.DrawText( y, (-10,y), color='blue')

# Draw Graph
for x in range(-100,100):
    y = math.sin(x/20)*50
    graph1.DrawCircle((x,y), 1, line_color='red', fill_color='red')

# Draw axis
graph2.DrawLine((-100,0), (100,0))
graph2.DrawLine((0,-100), (0,100))

for x in range(-100, 101, 20):
    graph2.DrawLine((x,-3), (x,3))
    if x != 0:
        graph2.DrawText( x, (x,-10), color='green')

for y in range(-100, 101, 20):
    graph2.DrawLine((-3,y), (3,y))
    if y != 0:
        graph2.DrawText( y, (-10,y), color='blue')

# Draw Graph
for x in range(-100,100):
    y = math.sin(x/20)*50
    graph2.DrawCircle((x,y), 1, line_color='green', fill_color='red')

while True:
    event, values = window.read()
    if event is None:
        break

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Read':
        f.write(values['-IN-'])
