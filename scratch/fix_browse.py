import sys

html_path = 'static/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

old_code = '''<div class="flex items-center space-x-2">
              <input type="text" id="doc-filename" placeholder="Document Title (e.g. OME345_AppliedDesignThinking_Lecture.txt)" class="flex-1 bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-xs text-slate-200 focus:border-indigo-500 focus:outline-none">
              <input type="file" id="file-picker" accept=".txt,.md,.py,.json,.csv,.js,.html,.css" class="hidden">
              <button type="button" id="btn-browse-file" class="btn-secondary">
                <i data-lucide="file-up" class="w-3.5 h-3.5 text-indigo-400"></i>
                <span>Browse File</span>
              </button>
            </div>'''

new_code = '''<button type="button" id="btn-browse-file" class="btn-secondary w-full py-3 border-dashed border-2 hover:border-indigo-500/50 text-sm">
              <i data-lucide="file-up" class="w-4 h-4 text-indigo-400"></i>
              <span>Browse & Select File</span>
            </button>
            <input type="file" id="file-picker" accept=".txt,.md,.py,.json,.csv,.js,.html,.css" class="hidden">
            <input type="text" id="doc-filename" placeholder="Document Title (e.g. OME345_AppliedDesignThinking_Lecture.txt)" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-xs text-slate-200 focus:border-indigo-500 focus:outline-none">'''

if old_code in html:
    html = html.replace(old_code, new_code)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Success")
else:
    print("Not found. Check whitespace.")