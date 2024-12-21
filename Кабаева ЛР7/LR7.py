import asyncio
import random
import time


# Функция для симуляции длительных вычислений
async def simulate_long_computation(expression):
    """Асинхронная функция для симуляции длительных вычислений."""
    await asyncio.sleep(random.uniform(0.1, 1.0))  # Симуляция задержки
    return eval(expression)


async def compute_expression(expression):
    """Асинхронная функция для вычисления математического выражения."""
    try:
        result = await simulate_long_computation(expression)
        return expression, result
    except Exception as e:
        return expression, f"Ошибка: {str(e)}"


async def compute_all(expressions):
    """Асинхронная функция для вычисления всех выражений."""
    tasks = [compute_expression(expr) for expr in expressions]
    results = await asyncio.gather(*tasks)
    return results


def display_results(results):
    """Функция для отображения результатов вычислений."""
    for expression, result in results:
        print(f"{expression} = {result}")


def generate_expressions(count):
    """Функция для генерации случайных математических выражений."""
    operators = ['+', '-', '*', '/']
    expressions = []
    for _ in range(count):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(operators)
        expression = f"{num1} {operator} {num2}"
        expressions.append(expression)
    return expressions


async def main():
    """Основная асинхронная функция."""
    start_time = time.time()
    expression_count = 20  # Количество выражений для вычисления
    expressions = generate_expressions(expression_count)

    print("Вычисление математических выражений...")
    results = await compute_all(expressions)

    display_results(results)
    print(f"Время выполнения: {time.time() - start_time:.2f} секунд")


if __name__ == "__main__":
    asyncio.run(main())
