import ParResPkgNew
print('initializing matlab_runtime copiler')

ParResinit = ParResPkgNew.initialize()
print('ParRes initialized')
ParRes = ParResinit.ParRes

print(ParRes)

ParResinit.terminate()
