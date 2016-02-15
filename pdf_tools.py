from PyPDF2 import PdfFileWriter, PdfFileReader
from pprint import pprint




def print_outline(document, depth=0, outline = []):
    tabs = ''
    for i in range(depth):
        tabs += '\t'
    for thing in document:
        if isinstance(thing, dict):
            outline.append([manual.getDestinationPageNumber(thing), thing['/Title']])
            print(tabs+thing['/Title'] + ' - ' + str(manual.getDestinationPageNumber(thing)))
        else:
            # pass
            print_outline(thing, depth + 1)
    return outline




def get_pages(outline, title, found=False, found_depth = None, depth=0, pages = []):
    def get_pages_rec(outline, title, found=False, found_depth = None, depth=0, pages = []):
        for thing in outline:
            # if found:
            if isinstance(thing, dict):
                if thing['/Title'] == title:
                    found = True
                    found_depth = depth
                if found:
                    pages.append(manual.getDestinationPageNumber(thing))
                    # print(str(manual.getDestinationPageNumber(thing)))
            else:
                pages = get_pages_rec(thing, title, found, found_depth, depth + 1, pages)
                if found_depth == depth:
                    found = False


        return(pages)



    found_depth = 0
    things = get_pages_rec(outline, title)
    ol = print_outline(outline)

    # print(max(things))
    next_chapter = 0
    for thing in ol:
        # print(str(thing[0]) + "Yeah")
        if thing[0] > max(things):
            next_chapter = thing[0]
            break

    print(things)
    print(next_chapter)
    things.append(next_chapter)


    if 0 in things:
        things.remove(0)
    return sorted(set(things))




def get_section(section):
    output = PdfFileWriter()
    pages = get_pages(manual.outlines, section)
    print(pages)
    for page in range(min(pages), max(pages)+1):
        # print(page)
        output.addPage(manual.getPage(page))
    f = section + ".pdf"

    outputStream = open(f, "wb")
    output.write(outputStream)

    print(f + " has been written.")

if __name__ == "__main__":
    pdffile = "CernerTrainingManual.pdf"
    manual = PdfFileReader(open(pdffile, "rb"))

    test = print_outline(manual.outlines)

    pprint(test)

    # get_pages(manual.outlines, "XVII Class Activities Answers")
    # get_section("XVII Class Activities")
    get_section("XX Practice 2")
    # get_section("XIII Comments")


