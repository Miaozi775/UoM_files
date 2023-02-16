data Color = Black | White deriving (Show, Eq)

data Quadtree = Leaf Int Color | Node Quadtree Quadtree Quadtree Quadtree -- clockwise from top left
                deriving (Show, Eq)

allBlack :: Int -> Quadtree
allBlack n = Leaf n Black

allWhite :: Int -> Quadtree
allWhite n = Leaf n White

clockwise :: Quadtree -> Quadtree -> Quadtree -> Quadtree -> Quadtree
clockwise a b c d = Node a b c d

anticlockwise :: Quadtree -> Quadtree -> Quadtree -> Quadtree -> Quadtree
anticlockwise a b c d = Node a d c b

-- clockwise (allBlack 1) (allBlack 1) (allWhite 1) (allWhite 1) == anticlockwise (allBlack 1) (allWhite 1) (allWhite 1) (allBlack 1)
-- clockwise (allBlack 1) (allBlack 1) (allWhite 1) (allWhite 1) /= anticlockwise (allBlack 1) (allBlack 1) (allWhite 1) (allBlack 1)

-- quardtree to matrix
quard2mat :: Quadtree -> [[Color]]
quard2mat (Leaf n c)     = [ [ c | _ <- [1..n] ] | _ <- [1..n] ]
quard2mat (Node a b c d) = zipWith (++) ma mb ++ zipWith (++) md mc
  where
    ma = quard2mat a
    mb = quard2mat b
    mc = quard2mat c
    md = quard2mat d

ndiffMat :: [[Color]] -> [[Color]]
ndiffMat mat = [ [ndiffElem (mat !! i !! j) (neighours mat (i,j)) | j <- [0..length mat - 1] ] | i <- [0..length mat - 1] ]

mat2quard :: [[Color]] -> Quadtree -> Quadtree
mat2quard mat (Leaf n _)
  -- all elements in mat are same
  | all (== head (head mat)) (concat mat) = Leaf n (head (head mat))
  | otherwise                             = Leaf n Black
mat2quard mat (Node a b c d) = 
    Node (mat2quard ma a) 
         (mat2quard mb b) 
         (mat2quard mc c) 
         (mat2quard md d)
  where
    n = length mat `div` 2
    l = length mat
    ma = [ [ mat !! i !! j | j <- [0..n - 1] ] | i <- [0..n - 1] ]
    mb = [ [ mat !! i !! j | j <- [n..l - 1] ] | i <- [0..n - 1] ]
    mc = [ [ mat !! i !! j | j <- [n..l - 1] ] | i <- [n..l - 1] ]
    md = [ [ mat !! i !! j | j <- [0..n - 1] ] | i <- [n..l - 1] ]

ndiff :: Quadtree -> Quadtree
ndiff q = mat2quard (ndiffMat (quard2mat q)) q

neighours :: [[Color]] -> (Int, Int) -> [Color]
neighours m (x, y) = fromMaybeList [ m !!? (x + dx, y + dy) | dx <- [-1, 0, 1], dy <- [-1, 0, 1], dx /= 0 || dy /= 0 ]

ndiffElem :: Color -> [Color] -> Color
ndiffElem c ncs = if all (== c) ncs then White else Black

(!!?) :: [[a]] -> (Int, Int) -> Maybe a
mat !!? (n, m)
  | n < 0 || n >= length mat        = Nothing
  | m < 0 || m >= length (mat !! n) = Nothing
  | otherwise                       = Just ((mat !! n) !! m)

fromMaybeList :: [Maybe a] -> [a]
fromMaybeList []           = []
fromMaybeList (Nothing:xs) = fromMaybeList xs
fromMaybeList (Just x:xs)  = x : fromMaybeList xs
