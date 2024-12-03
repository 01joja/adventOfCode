// use std::process::exit;



fn main(){

    let test_reports = read_and_parse("src/bin/day02.test");
    let test_result = part1(&test_reports);
    println!("test1: {test_result}");
    let test_result = part2(&test_reports);
    println!("test2: {test_result}");


    let reports = read_and_parse("src/bin/day02.data");
    let result = part1(&reports);
    println!("part1: {result}");
    let result = part2(&reports);
    println!("test2: {result}");

}

fn part1(reports: &Vec<Vec<i32>>) -> i32{
    let mut lower;
    let mut higher;
    let mut last_num;
    let mut result = 0;
    
    for row in reports{
        result += 1;
        lower = false;
        higher = false;
        last_num = 0;
        for num in row{
            if last_num == 0{
                last_num = *num;
                continue;
            }

            if last_num < *num && !lower && (last_num-*num).abs()<=3{
                higher = true;
            } else if last_num > *num && !higher && (last_num-*num).abs()<=3{
                lower = true;
            } else {
                result -=1;
                break;
            }
            last_num = *num;
        }
        
    }
    result
}


fn part2(reports: &Vec<Vec<i32>>) -> i32{
    let mut lower;
    let mut higher;
    let mut last_num;
    let mut result = 0;
    
    for row in reports{
        for skip in 0..row.len(){
            lower = false;
            higher = false;
            last_num = 0;
            let mut success = true;
            for i in 0..row.len(){
                if skip == i{
                    continue;
                }
                let num = row[i];
                if last_num == 0{
                    last_num = num;
                    continue;
                }

                if last_num < num && !lower && (last_num-num).abs()<=3{
                    higher = true;
                } else if last_num > num && !higher && (last_num-num).abs()<=3{
                    lower = true;
                } else {
                    success = false;
                    break;
                }
                last_num = num;
            }
            if success{
                result+=1;
                break;
            }
        }
    }
    result
}

// fn part2(reports: &Vec<Vec<i32>>) -> i32{
//     let mut result = 0;
//     for row in reports{
//         match manage_row(row, usize::MAX){
//             Ok(_) => {result+=1;},
//             Err(i) => {
//                 match manage_row(row, i){
//                     Ok(_) => {result+=1;},
//                     Err(j) => {
//                         if i == 1{
//                             match manage_row(row, 0){
//                                 Ok(_) => {result+=1;},
//                                 Err(_) => {},
//                             }
//                         }
//                         if i == 2{
//                             match manage_row(row, 1){
//                                 Ok(_) => {result+=1;},
//                                 Err(_) => {},
//                             }
//                         }
//                     },
//                 }
//             },
//         }
//     }
//     result
// }

// fn manage_row(row: &Vec<i32>,skip:usize) -> Result<(),usize>{
    
//     let mut lower= false;
//     let mut higher= false;
//     let mut last_num= 0;
//     let mut num = 0;
    
//     for i in 0..row.len(){
//         if i == skip{
//             continue;
//         }
//         num = row[i];
//         if last_num == 0{
//             last_num = num;
//             continue;
//         }

//         if last_num < num && !lower && (last_num-num).abs()<=3{
//             higher = true;
//         } else if last_num > num && !higher && (last_num-num).abs()<=3{
//             lower = true;
//         } else {
//             return Err(i);
//         }
//         last_num = num;
//     }
    
//     Ok(())
// }


fn read_and_parse<P>(path: P) -> Vec<Vec<i32>> 
where P: AsRef<std::path::Path>{
    let  contents = std::fs::read_to_string(path).unwrap();
    let mut data = vec![];
    for l in contents.split("\n"){
        let mut row = vec![];
        for n in l.split(" "){
            row.push(n.parse::<i32>().unwrap())
        }
        data.push(row)
    }
    data
}


