FILES :=        \
    .gitignore  \
    .travis.yml \
    IDB1.log    \
    IDB1.html \
    app/models.py   \
    app/tests.py    \
    IDB1.pdf

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

test:
    rm tests.out
    -coverage run    --branch app/tests.py >  tests.out 2>&1
	-coverage report -m                      >> tests.out
	cat tests.out

-$(PYLINT) TestCollatz.py
	-$(COVERAGE) run    --branch TestCollatz.py >  TestCollatz.tmp 2>&1
	-$(COVERAGE) report -m                      >> TestCollatz.tmp
	cat TestCollatz.tmp