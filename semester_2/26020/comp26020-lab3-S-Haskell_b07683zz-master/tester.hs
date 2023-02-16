-- This file is used to test your submission
-- it checks whether your submission will work with the automated testing script
-- but it does not provide many examples.
-- More testing examples will be provided on Blackboard
-- It needs to be pasted after your submission, which is what the script check_submission.hs does
-- before compiling and running

-- testing exercise 1

t1a = clockwise (allBlack 1) (allBlack 1) (allWhite 1) (allWhite 1) == anticlockwise (allBlack 1) (allWhite 1) (allWhite 1) (allBlack 1)

t1b = clockwise (allBlack 2) (anticlockwise (allBlack 1) (allWhite 1) (allWhite 1) (allBlack 1)) (allWhite 2) (allWhite 2) == anticlockwise (allBlack 2) (allWhite 2) (allWhite 2) (clockwise (allBlack 1) (allBlack 1) (allWhite 1) (allWhite 1))

t1c = clockwise (allBlack 1) (allBlack 1) (allWhite 1) (allWhite 1) /= anticlockwise (allWhite 1) (allWhite 1) (allWhite 1) (allBlack 1)

-- texting exercise 2

t2ai = (clockwise(clockwise(clockwise(allBlack 1)(allBlack 1)(allWhite 1)(allBlack 1))(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allWhite 1))(allWhite 2)(allBlack 2))(clockwise(allBlack 2)(allBlack 2)(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allWhite 1))(clockwise(allBlack 1)(allBlack 1)(allWhite 1)(allWhite 1)))(allWhite 4)(clockwise(allBlack 2)(clockwise(allBlack 1)(allBlack 1)(allWhite 1)(allBlack 1))(clockwise(allBlack 1)(allWhite 1)(allWhite 1)(allBlack 1))(allBlack 2)))

t2ao = (clockwise(clockwise(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(allBlack 2)(allBlack 2))(clockwise(allBlack 2)(allWhite 2)(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1)))(allBlack 4)(clockwise(allBlack 2)(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(allWhite 2)))


t2a = (ndiff t2ai) == t2ao


t2bi = (clockwise(clockwise(clockwise(allBlack 2)(allBlack 2)(clockwise(allBlack 1)(allBlack 1)(allWhite 1)(allBlack 1))(allBlack 2))(clockwise(clockwise(allBlack 1)(allBlack 1)(allWhite 1)(allBlack 1))(clockwise(allBlack 1)(allBlack 1)(allWhite 1)(allWhite 1))(allWhite 2)(allWhite 2))(clockwise(clockwise(allWhite 1)(allBlack 1)(allWhite 1)(allBlack 1))(clockwise(allBlack 1)(allWhite 1)(allBlack 1)(allWhite 1))(allWhite 2)(allWhite 2))(clockwise(allBlack 2)(allWhite 2)(allWhite 2)(clockwise(allBlack 1)(allWhite 1)(allWhite 1)(allBlack 1))))(clockwise(clockwise(clockwise(allBlack 1)(allBlack 1)(allWhite 1)(allWhite 1))(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allWhite 1))(allWhite 2)(allWhite 2))(clockwise(allBlack 2)(allBlack 2)(allBlack 2)(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allWhite 1)))(clockwise(clockwise(allWhite 1)(allWhite 1)(allWhite 1)(allBlack 1))(allBlack 2)(clockwise(allWhite 1)(allBlack 1)(allBlack 1)(allWhite 1))(allWhite 2))(clockwise(clockwise(allWhite 1)(allWhite 1)(allBlack 1)(allWhite 1))(clockwise(allBlack 1)(allBlack 1)(allWhite 1)(allWhite 1))(allWhite 2)(allWhite 2)))(clockwise(clockwise(allWhite 2)(allWhite 2)(clockwise(allWhite 1)(allWhite 1)(allBlack 1)(allBlack 1))(allWhite 2))(clockwise(allWhite 2)(clockwise(allWhite 1)(allBlack 1)(allBlack 1)(allWhite 1))(clockwise(allWhite 1)(allBlack 1)(allBlack 1)(allWhite 1))(allWhite 2))(clockwise(allWhite 2)(clockwise(allWhite 1)(allBlack 1)(allBlack 1)(allWhite 1))(allBlack 2)(clockwise(allBlack 1)(allWhite 1)(allBlack 1)(allBlack 1)))(clockwise(allWhite 2)(allBlack 2)(allBlack 2)(clockwise(allWhite 1)(allBlack 1)(allBlack 1)(allBlack 1))))(clockwise(clockwise(clockwise(allBlack 1)(allWhite 1)(allWhite 1)(allBlack 1))(allWhite 2)(allWhite 2)(clockwise(allBlack 1)(allWhite 1)(allWhite 1)(allBlack 1)))(clockwise(allWhite 2)(allWhite 2)(clockwise(allWhite 1)(allWhite 1)(allWhite 1)(allBlack 1))(clockwise(allWhite 1)(allWhite 1)(allBlack 1)(allWhite 1)))(clockwise(clockwise(allWhite 1)(allBlack 1)(allBlack 1)(allWhite 1))(clockwise(allBlack 1)(allWhite 1)(allWhite 1)(allBlack 1))(allBlack 2)(allBlack 2))(clockwise(clockwise(allBlack 1)(allWhite 1)(allBlack 1)(allBlack 1))(allWhite 2)(clockwise(allBlack 1)(allWhite 1)(allBlack 1)(allBlack 1))(allBlack 2))))

t2bo = (clockwise(clockwise(clockwise(allWhite 2)(allBlack 2)(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(allBlack 2))(clockwise(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(allBlack 2)(allBlack 2))(clockwise(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(allBlack 2)(allBlack 2))(clockwise(allBlack 2)(allBlack 2)(allBlack 2)(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))))(clockwise(clockwise(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(allBlack 2)(allBlack 2))(clockwise(allBlack 2)(allWhite 2)(allBlack 2)(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1)))(clockwise(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(allBlack 2)(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(allBlack 2))(clockwise(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(allBlack 2)(allBlack 2)))(clockwise(clockwise(allWhite 2)(allWhite 2)(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(allBlack 2))(clockwise(allWhite 2)(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(allBlack 2))(clockwise(allBlack 2)(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(allBlack 2)(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1)))(clockwise(allBlack 2)(allBlack 2)(allBlack 2)(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))))(clockwise(clockwise(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(allWhite 2)(allWhite 2)(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1)))(clockwise(allWhite 2)(allWhite 2)(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1)))(clockwise(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(allBlack 2)(allBlack 2))(clockwise(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(allBlack 2)(clockwise(allBlack 1)(allBlack 1)(allBlack 1)(allBlack 1))(allBlack 2))))

t2b = (ndiff t2bi) == t2bo

main =     print("Tests running...")
        >> print(if t1a then "Simple check for ex 1 passed!" else "Simple check for ex1 FAILED!")
        >> print(if t1c then "Inequality check for ex 1 passed!" else "Inequality check for ex1 FAILED!")
        >> print(if t1b then "Larger check for ex 1 passed!" else "Larger check for ex1 FAILED!")
        >> print(if t2a then "Small check for ex 2 passed!" else "Small check for ex2 FAILED!")
        >> print(if t2a then "Medium check for ex 2 passed!" else "Medium check for ex2 FAILED!")
--
