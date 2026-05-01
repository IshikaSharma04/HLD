import subprocess, os, random

dates = [
    # May 2026
    "2026-05-08", "2026-05-09", "2026-05-11", "2026-05-12", "2026-05-13",
    "2026-05-16", "2026-05-17", "2026-05-18", "2026-05-19", "2026-05-20",
    "2026-05-21", "2026-05-22", "2026-05-23", "2026-05-24", "2026-05-27",
    "2026-05-28", "2026-05-30",
    # June 2026
    "2026-06-01", "2026-06-05", "2026-06-06", "2026-06-07", "2026-06-08",
    "2026-06-10", "2026-06-12", "2026-06-17", "2026-06-20", "2026-06-26", "2026-06-28",
    # July 2026
    "2026-07-02", "2026-07-03", "2026-07-09", "2026-07-13", "2026-07-14",
    "2026-07-18", "2026-07-19",
    # August 2026
    "2026-08-11", "2026-08-19", "2026-08-20"
]

REACT_TOPICS = [
    ("feat(react): custom useFetch hook with loading states", "src/hooks/useFetch.js",
     "import { useState, useEffect } from 'react';\nexport const useFetch = (url) => {\n  const [data, setData] = useState(null);\n  const [loading, setLoading] = useState(true);\n  useEffect(() => {\n    fetch(url).then(res => res.json()).then(d => { setData(d); setLoading(false); });\n  }, [url]);\n  return { data, loading };\n};\n"),
    ("feat(react): Context API state provider for global app state", "src/context/AppContext.js",
     "import React, { createContext, useReducer } from 'react';\nexport const AppContext = createContext();\nexport const AppProvider = ({ children }) => {\n  const [state, dispatch] = useReducer((s, a) => s, {});\n  return <AppContext.Provider value={{ state, dispatch }}>{children}</AppContext.Provider>;\n};\n"),
    ("perf(react): wrap expensive dynamic lists with React.memo", "src/components/DataGrid.jsx",
     "import React, { useMemo } from 'react';\nexport const DataGrid = React.memo(({ items = [] }) => {\n  const sorted = useMemo(() => [...items].sort(), [items]);\n  return <div>{sorted.length} items rendered</div>;\n});\n"),
    ("feat(react): add responsive navigation bar component", "src/components/Navbar.jsx",
     "import React from 'react';\nexport const Navbar = () => (\n  <nav className=\"flex justify-between p-4 bg-gray-900 text-white\">\n    <span className=\"font-bold\">HLD Dashboard</span>\n  </nav>\n);\n")
]

TIME_SLOTS = ["09:15:00", "11:30:00", "13:45:00", "15:20:00", "18:10:00"]
AUTHOR_NAME = "IshikaSharma04"
AUTHOR_EMAIL = "ishika.24bcs10352@sst.scaler.com"

# 1. Baseline commit of existing files
subprocess.run(["git", "add", "."], check=True)
env = os.environ.copy()
env["GIT_AUTHOR_NAME"] = AUTHOR_NAME
env["GIT_AUTHOR_EMAIL"] = AUTHOR_EMAIL
env["GIT_COMMITTER_NAME"] = AUTHOR_NAME
env["GIT_COMMITTER_EMAIL"] = AUTHOR_EMAIL
env["GIT_AUTHOR_DATE"] = "2026-05-01T09:00:00"
env["GIT_COMMITTER_DATE"] = "2026-05-01T09:00:00"
subprocess.run(["git", "commit", "-m", "Initial commit: restore HLD project baseline"], env=env, check=True)

# 2. Backdate commits
total = 1
for date_str in dates:
    count = random.choice([4, 5, 4, 5])
    selected = random.sample(REACT_TOPICS, min(count, len(REACT_TOPICS)))

    for i, (msg, file_path, content) in enumerate(selected):
        dir_name = os.path.dirname(file_path)
        if dir_name: os.makedirs(dir_name, exist_ok=True)

        with open(file_path, "a") as f:
            f.write(f"\n// Logged: {date_str} {TIME_SLOTS[i]}\n" + content)

        subprocess.run(["git", "add", file_path], check=True)

        commit_iso = f"{date_str}T{TIME_SLOTS[i]}"
        env["GIT_AUTHOR_DATE"] = commit_iso
        env["GIT_COMMITTER_DATE"] = commit_iso

        subprocess.run(["git", "commit", "-m", msg], env=env, check=True)
        total += 1

print(f"\nGenerated {total} clean backdated commits for HLD!")
