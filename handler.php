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
           $pizzabill=+ 6
        }
        if ($pizzasize="extra-large") {
            $pizzabill=+ 10
        }
        $topping1 = "", "Would you like a topping Y or N:"
        if ($topping1= "N") {
            $subtotal= $pizzabill;
            echo "Subtotal: $", $subtotal;
            $tax= $pizzabill * 0.13;
            echo "Tax: $", $tax;
            $finalcost= $pizzabill * 1.13
            echo "Final Cost: $", $finalcost;
        }
        if ($topping1= "Y") {
            $toppingsbill1= 1
            echo "","Please select a topping: ";
            $topping2= "", "Would you like a second topping Y or N: ";
        }
