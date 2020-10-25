import subprocess , os
import psutil
import time


def on_terminate(program):
    print("terminated " , program.returncode)
    print(program.memory_info())


def RunSingleCpp(raw_code  , judge_input_file_name , judge_output_file_name , time_limit_milisec ):
    if not os.path.exists("Temp"):
        os.mkdir("Temp")

    raw_code_file = open(file = "Temp\\Solution.java" , mode = 'w' ,encoding= 'utf-8')
    raw_code_file.write(raw_code)
    raw_code_file.close()

    compile_log = open("Temp\\compile_log.txt" , 'w')

    program_name = "Temp\\Solution.class"

    if os.path.exists(program_name):
        os.remove(program_name)

    compile_command = ["javac", "-encoding", "UTF-8",  raw_code_file.name ]
    print( compile_command )
    subprocess.run(compile_command   , stderr=compile_log , capture_output = False )
    compile_log.close()

    print("compilation ended")

    #########  compilation log
    #run_log  = open(run_log.name , 'r')
    #print(run_log.read())


    if os.path.exists(program_name) == False :
        return "Compilation Error"

    run_command =  ["java" , "-cp" , "Temp" , "Solution" ]
    program_input = open(judge_input_file_name , 'r')
    program_output = open("Temp\\program_output.txt" , 'w')
    program_error = open("Temp\\Program_error.txt",'w')

    print(run_command)
    
    #program = subprocess.Popen(run_command , stdin = program_input , stdout= program_output , stderr= program_error  ) 
    program_psutil = psutil.Popen(run_command , stdin = program_input , stdout= program_output , stderr= program_error  )
    execution_time_ns = time.time_ns()
    try :
        program_psutil.wait(timeout=time_limit_milisec/1000.0)
        execution_time_ns = (time.time_ns() - execution_time_ns)
        execution_time_ms = execution_time_ns /1000000.0
        #print(program_psutil.memory_info())
    except psutil.TimeoutExpired as e:
        print(e.seconds)
        return "Time Limit Exceeded"
    

    if len(open(program_error.name , 'r' ).read()) > 0:
        return "Runtime Error"

    print("execution time " + str(execution_time_ms ) + " ms ")

    if open(judge_output_file_name , "r").read()  == open(program_output.name , 'r').read():
        return "Accepted"
    else: 
        return "Wrong Answer"


if __name__ == '__main__':
    raw_code = open("OJ\\Judge\\Solution.java" , 'r' , encoding= 'utf-8').read()
    print ( RunSingleCpp(raw_code  , 'OJ\\Judge\\input.txt' , 'OJ\\Judge\\output.txt' , 3000) )
