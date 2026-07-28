from pathlib import Path
import re

MAPPINGS = [
    (r'(?<![\\\w-])S-123(?![\w-])', r'\\terme{s123}'),
    (r'(?<![\\\w-])S-100(?![\w-])', r'\\terme{s100}'),
    (r'(?<![\\\w])GeoTIFF(?![\w])', r'\\terme{geotiff}'),
    (r'(?<![\\\w])GEOTIFF(?![\w])', r'\\terme{geotiff}'),
    (r'(?<![\\\w])DevOps(?![\w])', r'\\terme{devops}'),
    (r'(?<![\\\w])DEVOPS(?![\w])', r'\\terme{devops}'),
    (r'(?<![\\\w])GitOps(?![\w])', r'\\terme{gitops}'),
    (r'(?<![\\\w])GITOPS(?![\w])', r'\\terme{gitops}'),
    (r'(?<![\\\w])SHOM(?![\w])', r'\\terme{shom}'),
    (r'(?<![\\\w])BDMR(?![\w])', r'\\terme{bdmr}'),
    (r'(?<![\\\w])FCU(?![\w])', r'\\terme{fcu}'),
    (r'(?<![\\\w])GDAL(?![\w])', r'\\terme{gdal}'),
    (r'(?<![\\\w])SVN(?![\w])', r'\\terme{svn}'),
    (r'(?<![\\\w])POC(?![\w])', r'\\terme{poc}'),
    (r'(?<![\\\w])ENC(?![\w])', r'\\terme{enc}'),
    (r'(?<![\\\w])RSX(?![\w])', r'\\terme{rsx}'),
    (r'(?<![\\\w])SMDSM(?![\w])', r'\\terme{smdsm}'),
    (r'(?<![\\\w])XSD(?![\w])', r'\\terme{xsd}'),
    (r'(?<![\\\w])UML(?![\w])', r'\\terme{uml}'),
    (r'(?<![\\\w])JWT(?![\w])', r'\\terme{jwt}'),
    (r'(?<![\\\w])CRUD(?![\w])', r'\\terme{crud}'),
    (r'(?<![\\\w])DTO(?![\w])', r'\\terme{dto}'),
    (r'(?<![\\\w])ORM(?![\w])', r'\\terme{orm}'),
    (r'(?<![\\\w])REST(?![\w])', r'\\terme{rest}'),
    (r'(?<![\\\w])API(?![\w])', r'\\terme{api}'),
    (r'(?<![\\\w])RLS(?![\w])', r'\\terme{rls}'),
    (r'(?<![\\\w])RGPD(?![\w])', r'\\terme{rgpd}'),
    (r'(?<![\\\w])OWASP(?![\w])', r'\\terme{owasp}'),
    (r'(?<![\\\w])CI(?![\w])', r'\\terme{ci}'),
    (r'(?<![\\\w])CD(?![\w])', r'\\terme{cd}'),
]

SKIP_PREFIXES = (
    r'\chapter', r'\section', r'\subsection', r'\subsubsection',
    r'\paragraph', r'\caption', r'\label', r'\begin', r'\end',
    r'\includegraphics', r'\lst', r'\newcommand', r'\renewcommand',
)

INLINE_CODE = re.compile(r'\\texttt\{[^{}]*\}|\\lstinline(?:\[[^]]*\])?(.)(.*?)\1')


def protect_inline_code(line: str):
    protected = []

    def repl(match):
        token = f'@@PROTECTED_{len(protected)}@@'
        protected.append(match.group(0))
        return token

    return INLINE_CODE.sub(repl, line), protected


def restore(line: str, protected):
    for i, text in enumerate(protected):
        line = line.replace(f'@@PROTECTED_{i}@@', text)
    return line


def transform(source: str) -> str:
    lines = source.splitlines(keepends=True)
    out = []
    in_listing = False

    for line in lines:
        stripped = line.lstrip()

        if stripped.startswith(r'\begin{lstlisting}') or stripped.startswith(r'\begin{verbatim}'):
            in_listing = True
            out.append(line)
            continue

        if stripped.startswith(r'\end{lstlisting}') or stripped.startswith(r'\end{verbatim}'):
            in_listing = False
            out.append(line)
            continue

        if in_listing or stripped.startswith('%') or stripped.startswith(SKIP_PREFIXES):
            out.append(line)
            continue

        work, protected = protect_inline_code(line)

        # Les occurrences déjà balisées ne doivent jamais être retraitées.
        chunks = re.split(r'(\\terme\{[^{}]+\})', work)
        for idx in range(0, len(chunks), 2):
            chunk = chunks[idx]
            for pattern, replacement in MAPPINGS:
                chunk = re.sub(pattern, replacement, chunk)
            chunks[idx] = chunk

        out.append(restore(''.join(chunks), protected))

    return ''.join(out)


def main():
    for path in sorted(Path('sections').glob('*.tex')):
        source = path.read_text(encoding='utf-8')
        result = transform(source)
        if result != source:
            path.write_text(result, encoding='utf-8')


if __name__ == '__main__':
    main()
