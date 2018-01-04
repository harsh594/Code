bool isPalindrome(int x) {
    int rev;
     if(x < 0 || (x % 10 == 0 && x != 0))
       return false;
    
    while(rev<x){
     rev=rev*10+x%10;
        x=x/10;
    }
    if (x==rev||x==rev/10)
        return true;
return false;
}

