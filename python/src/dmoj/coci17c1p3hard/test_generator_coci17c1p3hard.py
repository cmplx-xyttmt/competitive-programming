import random
import string


def generate_test_case(num_queries, max_len=10):
    queries = []
    # To make queries meaningful, we'll keep track of some added passwords
    added_passwords = []

    print(num_queries)

    for _ in range(num_queries):
        # Randomly choose query type (1: Insert, 2: Query)
        # We weigh it so we don't query an empty database too often early on
        q_type = 1 if not added_passwords or random.random() < 0.5 else 2

        if q_type == 1:
            length = 10
            pwd = ''.join(random.choices(string.ascii_lowercase, k=length))
            added_passwords.append(pwd)
            print(f"1 {pwd}")
        else:
            # Occasionally query a random string,
            # but usually query a substring of an existing password to get hits
            if random.random() < 0.7:
                base_pwd = random.choice(added_passwords)
                start = random.randint(0, len(base_pwd) - 1)
                end = random.randint(start + 1, len(base_pwd))
                query_str = base_pwd[start:end]
            else:
                length = 10
                query_str = ''.join(random.choices(string.ascii_lowercase, k=length))

            print(f"2 {query_str}")


# Example usage: Generate 20 queries
if __name__ == "__main__":
    generate_test_case(100000)
