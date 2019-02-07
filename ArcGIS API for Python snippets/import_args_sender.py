import arcpy
import import_args_reciever
import 

input_string = 'hello world'

arcpy.SetParameterAsText(0, input_string)
import_args_reciever.main()