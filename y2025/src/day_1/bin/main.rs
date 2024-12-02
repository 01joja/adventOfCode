
use std::iter::zip;
// use std::env;
// use std::fs;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::vec;


fn main(){

    let mut l = vec![];
    let mut r = vec![];
    if let Ok(lines) = read_lines("src/day_1/data/data1") {
        // Consumes the iterator, returns an (Optional) String
        for line in lines.flatten() {
            if let Some((left,right)) = line.split_once("   "){
                l.push(left.parse::<i32>().unwrap());
                r.push(right.parse::<i32>().unwrap());
            } else {
                panic!("No x-mas for you");
            }
        }
    }

    let res = part1(&mut l, &mut r);
    println!("result part1: {res}");
    let res = part2(&mut l,&mut r);
    println!("result part2: {res}");

}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn part1(left:&mut Vec<i32>, right:&mut Vec<i32>) -> i32{
    left.sort();
    right.sort();
    let iter = zip(left,right);
    let mut r=0;
    for i in iter{
        r += (*i.0-*i.1).abs();
    }
    r
}

fn part2( left: &mut Vec<i32>,  right: &mut Vec<i32>) -> i32{
    right.reverse();
    let mut r=0;
    let mut last_l = 0;
    let mut last_r = 0;
    let mut times = 0;
    // let mut panic_at = 0;
    for i in left{

        // if panic_at == 20{
        //     panic!("woops!")
        // }
        // panic_at += 1;

        if last_l == *i{
            r+= last_l*times;
            continue;
        } else {
            last_l = *i;
        }

        times = 0;
        while last_r <= last_l && right.len() > 1{
            if last_l == last_r{
                times+=1;
            }
            last_r = right.pop().unwrap();
        }
        r+=last_l*times;
    }
    r
}







