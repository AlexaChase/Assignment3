<!DOCTYPE html>
<html>
    <head>
        <title>Pizza Order</title>
    </head>
    
    <body>
        <?php
        echo "Welcome, please choose the size of the pizza: ";
        echo "large or extra-large: ";
        $pizzasize= "";
        if ($pizzasize="small") {
            echo "Error, this size is not available";
        }
        if ($pizzasize="medium") {
            echo "Error, this size is not available";
        }
        if ($pizzasize="large") {
           $pizzabill=+ 6;
           $topping1 = "" ("Would you like a topping Y or N:");
        }
        if ($pizzasize="extra-large") {
            $pizzabill=+ 10;
            $topping1 = "" ("Would you like a topping Y or N:");
        }
        
        if ($topping1= "N") {
            $subtotal= $pizzabill;
            echo "Subtotal: $", $subtotal;
            $tax= $pizzabill * 0.13;
            echo "Tax: $", $tax;
            $finalcost= $pizzabill * 1.13;
            echo "Final Cost: $", $finalcost;
        }
        if ($topping1= "Y") {
            $toppingsbill1= 1;
            echo ""("Please select a topping: ");
            $topping2= "" ("Would you like a second topping Y or N: ");
        }
            if ($topping2= "N") {
                $subtotal= $pizzabill + $topping1;
                echo "Subtotal: $", $subtotal;
                $tax= ($pizzabill + $topping1) * 0.13;
                echo "Tax: $", $tax;
                $finalcost= ($pizzabill + $topping1) * 1.13;
                echo "Final Cost: $", $finalcost;
            }
            if ($topping2= "Y") {
                $toppingsbill2= 1.75;
                echo ""("Please select a topping: ");
                $topping3= "" ("Would you like a third topping Y or N: ");
            }
            if ($topping3= "N"){
                $subtotal= $pizzabill + $toppingsbill1 + $toppingsbill2;
                echo "Subtotal: $", $subtotal;
                $tax= ($pizzabill + $toppingsbill1 + $toppingsbill2) * 0.13;
                echo "Tax: $", $tax;
                $finalcost= ($pizzabill + $toppingsbill1 + $toppingsbill2) * 1.13;
                echo "Final Cost: $", $finalcost;
            }
            if ($topping3= "Y"){
                $toppingsbill3= 2.50;
                echo "", "Please select a topping:";
                $topping4= "" ("Would you like a third topping Y or N: ");
            }
                if ($topping4== "N"){
                    $subtotal= $pizzabill + $toppingsbill1 + $toppingsbill2 + $toppingsbill3;
                    echo "Subtotal: $", $subtotal;
                    $tax= ($pizzabill + $toppingsbill1 + $toppingsbill2 + $toppingsbill3) * 0.13;
                    echo "Tax: $", $tax;
                    $finalcost= ($pizzabill + $toppingsbill1 + $toppingsbill2 + $toppingsbill3) * 1.13;
                    echo "Final Cost: $", $finalcost;
                }
                if ($topping4== "Y") {
                    $toppingsbill4=+ 3.35;
                    echo ""("Please select a topping: ");
                    $subtotal= $pizzabill + $toppingsbill1 + $toppingsbill2 + $toppingsbill3 + $toppingsbill4;
                    echo "Subtotal: $",$subtotal;
                    $tax= ($pizzabill + $toppingsbill1 + $toppingsbill2 + $toppingsbill3 + $toppingsbill4) * 0.13;
                    echo "Tax: $", $tax;
                    $finalcost= ($pizzabill + $toppingsbill1 + $toppingsbill2 + $toppingsbill3 + $toppingsbill4) * 1.13;
                    echo $finalcost;
                }
        ?>
    </body>
</html>