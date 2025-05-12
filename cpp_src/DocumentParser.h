#pragma once
#include <vector>
#include <string>

struct Document {
    std:: string input;
    std:: string output;
};

std::vector<Document> load_csv(const std::string& filename);