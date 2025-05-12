#include "DocumentParser.h"
#include "csv.h"
#include <string>
#include <vector>
#include <iostream>


std::vector<Document> load_csv(const std::string& filename) {
    std::vector<Document> docs;
    try {
        io::CSVReader<2, io::trim_chars<>, io::double_quote_escape<',','\"'>> in(filename);
        in.read_header(io::ignore_extra_column, "input", "output");
        std::string input, output;
        while (in.read_row(input, output)) {
            docs.push_back({input, output});
        }
    } catch (const io::error::escaped_string_not_closed& e) {
        std::cerr << "CSV parsing error: " << e.what() << std::endl;
    }
    return docs;
}