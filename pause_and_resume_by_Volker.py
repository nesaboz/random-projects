from System.Threading import CancellationTokenSource
from threading import Event
import async

ThreadControls=[]
numberOfThreads = 4
for i in range(numberOfThreads):
	ThreadControls.append([Event(),CancellationTokenSource()])

# use in code wherever you want to allow pausing or cancelling of a thread, you might place that line in every other line of your code :)
def pause_and_cancel_point(ThreadID):
	ThreadControls[ThreadID][0].wait()
	ThreadControls[ThreadID][1].Token.ThrowIfCancellationRequested()


# to abort thread
def cancel(ThreadID):
	print('Cancelling thread '+ str(ThreadID)+'.')
	ThreadControls[ThreadID][1].Cancel()


# to pause thread
def pause(ThreadID):
	print('Pausing thread '+ str(ThreadID)+'.')
	ThreadControls[ThreadID][0].clear()


# to resume thread
def resume(ThreadID):
	print('Resuming thread '+ str(ThreadID)+'.')
	ThreadControls[ThreadID][0].set()


def exampleThread(ThreadID):
	print('ExampleThread '+ str(ThreadID)+ ' started.')
	#doing something long with pause and cancel points
	for i in range (20):
		cmd.Delay(1)
		pause_and_cancel_point(ThreadID)
	print('ExampleThread '+ str(ThreadID)+ ' finished.')


def exampleProgram():
	task0=async(exampleThread)(0)
	task1=async(exampleThread)(1)
	cmd.Delay(2)
	pause(1)
	cmd.Delay(2)
	task2=async(exampleThread)(2)
	cmd.Delay(2)
	resume(1)
	cmd.Delay(2)
	cancel(0)
	cmd.Delay(2)
	cancel(1)