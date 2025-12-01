# file: server.py
import zmq
import sys

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print("Server started... Press Ctrl+C to exit.")

    try:
        while True:
            msg = socket.recv_string()
            print(f"Received: {msg}")
            socket.send_string("OK")
    except KeyboardInterrupt:
        print("Shutting down server...")
    finally:
        socket.close()  # cleanup
        context.term()  # cleanup
        sys.exit(0)     # exit process

if __name__ == "__main__":
    main()
