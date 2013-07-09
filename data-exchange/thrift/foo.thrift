struct Balance {
    1: double credit,
    2: string currency
}

struct Portout {
    1: string status
}

service FooService {
    string ping(),
    Balance balance(1: i32 msisdn),
    map<string, string> portin(1: i32 msisdn),
    Portout portout(1: i32 msisdn),
    map<string, string> addcredit(1: i32 msisdn, 2: i32 amount),
}

