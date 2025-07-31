def compareVersion(version1Var: str, version2Var: str):
    version1Parts = list(map(int, version1Var.split(".")))
    version2Parts = list(map(int, version2Var.split(".")))

    return abs(version1Parts[0] - version2Parts[0]) * -1

version1 = ["1.01","1.0","0.1"]
version2 = ["1.01","1.0","1.1"]
print(compareVersion(version1, version2))
