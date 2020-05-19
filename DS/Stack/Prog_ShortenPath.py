# O(n) time | O(n) space
def shortenPath(path):
    startsWithSlash = path[0] == "/"
    tokens = filter(isImportantToken, path.split("/"))
    stack = []

    if startsWithSlash:
        stack.append("")

    for token in tokens:
        if token == "..":
            if len(stack) == 0 or stack[-1] == "..":
                stack.append(token)
            elif stack[-1] == "":
                continue
            elif stack[-1] != "":
                stack.pop()
        else:
            stack.append(token)

    if len(stack) == 1 and stack[0] == "":
        return "/"
    return "/".join(stack)


def isImportantToken(token):
    return len(token) > 0 and token != "."


def testShortenPath(testcasenumber, path):
    print(
        f'testcase_{testcasenumber} Path: {path} Shorten Path: {shortenPath(path)}')


if __name__ == '__main__':
    testcases = [
        {"path": "/foo/../test/../test/../foo//bar/./baz"},
        {"path": "/foo/bar/baz"},
        {"path": "foo/bar/baz"},
        {"path": "/../../foo/bar/baz"},
        {"path": "../../foo/bar/baz"},
        {"path": "/../../foo/../../bar/baz"},
        {"path": "../../foo/../../bar/baz"},
        {"path": "/foo/./././bar/./baz///////////test/../../../kappa"},
        {
            "path": "../../../this////one/./../../is/../../going/../../to/be/./././../../../just/eight/double/dots/../../../../../.."
        },
        {
            "path": "/../../../this////one/./../../is/../../going/../../to/be/./././../../../just/a/forward/slash/../../../../../.."
        },
        {
            "path": "../../../this////one/./../../is/../../going/../../to/be/./././../../../just/eight/double/dots/../../../../../../foo"
        },
        {
            "path": "/../../../this////one/./../../is/../../going/../../to/be/./././../../../just/a/forward/slash/../../../../../../foo"
        },
        {"path": "foo/bar/.."},
        {"path": "./foo/bar"},
        {"path": "foo/../.."},
        {"path": "/"}
    ]

    caseno = 1
    for testcase in testcases:
        testShortenPath(caseno, testcase["path"])
        caseno += 1
