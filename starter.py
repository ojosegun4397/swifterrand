from errandapp import app
# from errandapp import socketio
from errandapp.useroutes import socketio






if __name__=='__main__':

    app.run(port=8086, debug=True)
    socketio.run(app, debug=True)