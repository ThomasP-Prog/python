"""
Describe final_report.py: Imports report_generator. Defines a sample document text string. 
Calls report_generator.generate_summary with a title and the sample text, then prints the returned summary string."""

import report_generator as rg

def main():
    """main function"""
    sample_doc = "This is a sample document for testing the text analyzer module."
    report_title = "Analysis of Sample Document"
    print(rg.generate_summary(report_title,sample_doc))

if __name__ == "__main__":
    main()