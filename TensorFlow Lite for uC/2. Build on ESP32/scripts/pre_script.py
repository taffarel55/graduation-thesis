Import("env")

print("Getting tensorflow lite model")

env.Execute("cp '../1. Creating model/sine_model.cc' ./src/sine_model.cc")
env.Execute("cp '../1. Creating model/sine_model.h' ./include/sine_model.h")
