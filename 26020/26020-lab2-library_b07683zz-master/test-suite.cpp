#define CATCH_CONFIG_MAIN

#include "catch.h"
#include "library.h"

#include <stdio.h>
#include <unistd.h>
#include <iostream>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

TEST_CASE("constructors and getters") {
    /* Simply instantiate some documents and check that the getters return
     * the right value for the attributes of the created objects */

    Novel n1 = Novel("Harry Potter", "J. K. Rowling", 1997, 1);
    CHECK(!strcmp(n1.getTitle(), "Harry Potter"));
    CHECK(!strcmp(n1.getAuthor(), "J. K. Rowling"));
    CHECK(n1.getYear() == 1997);
    CHECK(n1.getQuantity() == 1);

    Comic c1 = Comic("Watchmen", "Alan Moore", 1, 1986, 10);
    CHECK(!strcmp(c1.getTitle(), "Watchmen"));
    CHECK(!strcmp(c1.getAuthor(), "Alan Moore"));
    CHECK(c1.getYear() == 1986);
    CHECK(c1.getQuantity() == 10);
    CHECK(c1.getIssue() == 1);

    Magazine m1 = Magazine("The New Yorker", 1, 1925, 20);
    CHECK(!strcmp(m1.getTitle(), "The New Yorker"));
    CHECK(m1.getIssue() == 1);
    CHECK(m1.getYear() == 1925);
    CHECK(m1.getQuantity() == 20);
}

TEST_CASE("setters") {
    Library l;

    Novel n1 = Novel("Harry Potter", "J. K. Rowling", 1997, 1);
    n1.updateQuantity(30);
    CHECK(n1.getQuantity() == 30);

    Comic c1 = Comic("Watchmen", "Alan Moore", 1, 1986, 10);
    c1.updateIssue(2);
    CHECK(c1.getIssue() == 2);

    Magazine m1 = Magazine("The New Yorkzz", 1, 1925, 20);
    m1.updateTitle("The New Yorker");
    CHECK(!strcmp(m1.getTitle(), "The New Yorker"));
}

TEST_CASE("library construction") {
    Library l;

    Novel n1 = Novel("Harry Potter", "J. K. Rowling", 1997, 1);
    Novel n2 = Novel("Watership Down", "Richard Adams", 1972, 2);

    Comic c1 = Comic("Watchmen", "Alan Moore", 1, 1986, 10);
    Magazine m1 = Magazine("The New Yorker", 1, 1925, 20);

    REQUIRE(!l.addDocument(&n1));
    REQUIRE(!l.addDocument(&n2));
    REQUIRE(!l.addDocument(&c1));
    REQUIRE(!l.addDocument(&m1));

    CHECK(l.countDocumentOfType(DOC_NOVEL) == 2);
    CHECK(l.countDocumentOfType(DOC_COMIC) == 1);
    CHECK(l.countDocumentOfType(DOC_MAGAZINE) == 1);

}

TEST_CASE("removing documents from library") {
    Library l;

    Novel n1 = Novel("Harry Potter", "J. K. Rowling", 1997, 1);
    Novel n2 = Novel("Watership Down", "Richard Adams", 1972, 2);

    Comic c1 = Comic("Watchmen", "Alan Moore", 1, 1986, 10);
    Magazine m1 = Magazine("The New Yorker", 1, 1925, 20);

    REQUIRE(!l.addDocument(&n1));
    REQUIRE(!l.addDocument(&n2));
    REQUIRE(!l.addDocument(&c1));
    REQUIRE(!l.addDocument(&m1));

    CHECK(l.countDocumentOfType(DOC_NOVEL) == 2);
    CHECK(l.countDocumentOfType(DOC_COMIC) == 1);
    CHECK(l.countDocumentOfType(DOC_MAGAZINE) == 1);

    CHECK(!(l.delDocument("Watership Down")));
    CHECK(!(l.delDocument("Watchmen")));
    CHECK((l.delDocument("Watchmen")));

    CHECK(l.countDocumentOfType(DOC_NOVEL) == 1);
    CHECK(l.countDocumentOfType(DOC_COMIC) == 0);
    CHECK(l.countDocumentOfType(DOC_MAGAZINE) == 1);
}

TEST_CASE("object-level print functions") {
    char printed_n1[128], printed_n2[128], printed_c1[128], printed_m1[128];
    char expected_n1[] = "Novel, title: Harry Potter, author: J. K. Rowling, " \
                         "year: 1997, quantity: 1\n";
    char expected_n2[] = "Novel, title: Watership Down, author: Richard " \
                         "Adams, year: 1972, quantity: 2\n";
    char expected_c1[] = "Comic, title: Watchmen, author: Alan Moore, " \
                         "issue: 1, year: 1986, quantity: 10\n";
    char expected_m1[] = "Magazine, title: The New Yorker, issue: 1, " \
                         "year: 1925, quantity: 20\n";

#define CHECK_STDOUT(obj) { \
    memset(printed_##obj, 0x0, 128); \
    lseek(STDOUT_FILENO, 0, SEEK_SET); \
    obj.print(); \
    lseek(STDOUT_FILENO, 0, SEEK_SET); \
    read(STDOUT_FILENO, printed_##obj, strlen(expected_##obj)); \
    printed_##obj[strlen(expected_##obj)] = '\0'; \
}

    int original_stdout = dup(STDOUT_FILENO);
    int tmpfd = open("/tmp/", O_RDWR | O_TMPFILE, S_IRUSR | S_IWUSR);
    REQUIRE(tmpfd != -1);

    Novel n1 = Novel("Harry Potter", "J. K. Rowling", 1997, 1);
    Novel n2 = Novel("Watership Down", "Richard Adams", 1972, 2);
    Comic c1 = Comic("Watchmen", "Alan Moore", 1, 1986, 10);
    Magazine m1 = Magazine("The New Yorker", 1, 1925, 20);

    /* What I'm doing here is a bit tricky and you don't need to understand
     * all the details. Long story short I am redirecting the standard output
     * into a file in order to be able to read that file and check that what
     * is normally printed in the standard output is correct (there is no
     * easy way to read the standard output from C code */
    dup2(tmpfd, STDOUT_FILENO);
    close(tmpfd);

    CHECK_STDOUT(n1);
    CHECK_STDOUT(n2);
    CHECK_STDOUT(c1);
    CHECK_STDOUT(m1);

    dup2(original_stdout, STDOUT_FILENO);
    CHECK(!strcmp(printed_n1, expected_n1));
    CHECK(!strcmp(printed_n2, expected_n2));
    CHECK(!strcmp(printed_c1, expected_c1));
    CHECK(!strcmp(printed_m1, expected_m1));
}

TEST_CASE("library-level print function") {
    char printed[512];
    char expected[] = "Novel, title: Harry Potter, " \
        "author: J. K. Rowling, year: 1997, quantity: 1\n" \
        "Novel, title: Watership Down, author: Richard " \
        "Adams, year: 1972, quantity: 2\n" \
        "Comic, title: Watchmen, author: Alan Moore, " \
        "issue: 1, year: 1986, quantity: 10\n" \
        "Magazine, title: The New Yorker, issue: 1, " \
        "year: 1925, quantity: 20\n";

    Novel n1 = Novel("Harry Potter", "J. K. Rowling", 1997, 1);
    Novel n2 = Novel("Watership Down", "Richard Adams", 1972, 2);
    Comic c1 = Comic("Watchmen", "Alan Moore", 1, 1986, 10);
    Magazine m1 = Magazine("The New Yorker", 1, 1925, 20);

    memset(printed, 0x0, 512);

    Library l;
    REQUIRE(!l.addDocument(&n1));
    REQUIRE(!l.addDocument(&n2));
    REQUIRE(!l.addDocument(&c1));
    REQUIRE(!l.addDocument(&m1));

    int original_stdout = dup(STDOUT_FILENO);
    int tmpfd = open("/tmp/", O_RDWR | O_TMPFILE, S_IRUSR | S_IWUSR);
    REQUIRE(tmpfd != -1);

    dup2(tmpfd, STDOUT_FILENO);
    close(tmpfd);

    lseek(STDOUT_FILENO, 0, SEEK_SET);
    l.print();
    lseek(STDOUT_FILENO, 0, SEEK_SET); \
    read(STDOUT_FILENO, printed, strlen(expected)); \
    printed[strlen(expected)] = '\0'; \

    dup2(original_stdout, STDOUT_FILENO);
    CHECK(!strcmp(printed, expected));
}

TEST_CASE("CSV file dump") {
    Library l;
    int buf_size = 512, fd, bytes_read;
    char content_read[buf_size];
    char expected[] = "novel,Harry Potter,J. K. Rowling,,1997,1\n"
            "novel,Watership Down,Richard Adams,,1972,2\n"
            "comic,Watchmen,Alan Moore,1,1986,10\n"
            "magazine,The New Yorker,,1,1925,20\n";
    char output_file[] = "output.csv";

    Novel n1 = Novel("Harry Potter", "J. K. Rowling", 1997, 1);
    Novel n2 = Novel("Watership Down", "Richard Adams", 1972, 2);
    Comic c1 = Comic("Watchmen", "Alan Moore", 1, 1986, 10);
    Magazine m1 = Magazine("The New Yorker", 1, 1925, 20);

    REQUIRE(!l.addDocument(&n1));
    REQUIRE(!l.addDocument(&n2));
    REQUIRE(!l.addDocument(&c1));
    REQUIRE(!l.addDocument(&m1));

    remove(output_file); /* (ignore errors) */
    REQUIRE(!l.dumpCSV(output_file));

    fd = open(output_file, O_RDONLY);
    REQUIRE(fd != -1);
    bytes_read = read(fd, content_read, buf_size);
    REQUIRE(bytes_read <= buf_size);
    close(fd);

    content_read[bytes_read] = '\0';
    CHECK(!strcmp(content_read, expected));
}

TEST_CASE("borrow-return functions") {
    Library l;
    int n1_num = 1, c1_num = 10;
    char n1_title[] = "Harry Potter", c1_title[] = "Watchmen";

    Novel n1 = Novel(n1_title, "J. K. Rowling", 1997, n1_num);
    Comic c1 = Comic(c1_title, "Alan Moore", 1, 1986, c1_num);

    REQUIRE(!l.addDocument(&n1));
    REQUIRE(!l.addDocument(&c1));

    for(int i=0; i<n1_num; i++)
        CHECK(!l.borrowDoc(n1_title));
    CHECK(l.borrowDoc(n1_title));
    CHECK(!l.returnDoc(n1_title));
    CHECK(!l.borrowDoc(n1_title));

    for(int i=0; i<c1_num; i++)
        CHECK(!l.borrowDoc(c1_title));
    CHECK(l.borrowDoc(c1_title));
    CHECK(!l.returnDoc(c1_title));
    CHECK(!l.borrowDoc(c1_title));

    CHECK(l.borrowDoc("The Neverending Story"));
    CHECK(l.returnDoc("Lord of the Ring"));
}
