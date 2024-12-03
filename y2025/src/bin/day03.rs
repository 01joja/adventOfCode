
use regex::Regex;


fn main(){

    let test_result = part1("src/bin/day03.test");
    println!("test1 result: {test_result}");
    let result = part1("src/bin/day03.data");
    println!("part1: {result}");
    
    let test_result = part2("src/bin/day03.test2");
    println!("test2 result: {test_result}");
    let result = part2("src/bin/day03.data");
    println!("part2: {result}");
}


fn part1<P>(path: P) -> i32 
where P: AsRef<std::path::Path>{
    let hay = std::fs::read_to_string(path).unwrap();
    let re = Regex::new(r"mul\([0-9]{0,3},[0-9]{0,3}\)").unwrap();
    
    let matches: Vec<_> = re.find_iter(&hay).map(|m| m.as_str()).collect();

    let mut res = 0;
    for s in matches{
        let (f,l) = s.split_once(",").unwrap();
        let (_,n1) = f.split_once("(").unwrap();
        let (n2,_) = l.split_once(")").unwrap();
        let r = n1.parse::<i32>().unwrap()*n2.parse::<i32>().unwrap();
        res+=r;
    }

    res
}

fn part2<P>(path: P) -> i32 
where P: AsRef<std::path::Path>{
    let hay = std::fs::read_to_string(path).unwrap();
    hay.split("do_not()")


    let re = Regex::new(r"mul\([0-9]{0,3},[0-9]{0,3}\)").unwrap();
    
    // let matches: Vec<_> = re.find_iter(&hay).map(|m| m.as_str()).collect();

    // let mut res = 0;
    // for s in matches{
    //     let (f,l) = s.split_once(",").unwrap();
    //     let (_,n1) = f.split_once("(").unwrap();
    //     let (n2,_) = l.split_once(")").unwrap();
    //     let r = n1.parse::<i32>().unwrap()*n2.parse::<i32>().unwrap();
    //     res+=r;
    // }

    // res
    5
}

