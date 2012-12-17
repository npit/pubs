from .. import repo


def parser(subparsers, config):
    parser = subparsers.add_parser('add', help='add a paper to the repository')
    parser.add_argument('pdffile', help='pdf or ps file')
    parser.add_argument('bibfile', help='bibtex, bibtexml or bibyaml file')
    return parser

def command(config, pdffile, bibfile):
    """
    :param pdffilepath  path (no url yet) to a pdf or ps file
    :param bibtex       bibtex file (in .bib, .bibml or .yaml format.
    """
    rp = repo.Repository()
    rp.add_paper_from_paths(pdffile, bibfile)