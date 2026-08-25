#include "CSVWriter.h"

CSVWriter::CSVWriter(const std::string& filename)
{
    file.open(filename);
}

CSVWriter::~CSVWriter()
{
    file.close();
}

void CSVWriter::writeHeader(const std::string& header)
{
    file << header;
    file << std::endl;
}

void CSVWriter::writeRow(const std::string& row)
{
    file << row;
    file << std::endl;
}