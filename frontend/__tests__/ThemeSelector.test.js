import { render, fireEvent } from '@testing-library/react'
import ThemeSelector from '../components/ThemeSelector'
test('Tema değiştirilebilir', () => {
  const setTheme = jest.fn()
  const { getByText } = render(<ThemeSelector theme="light" setTheme={setTheme} />)
  fireEvent.click(getByText("Galaksi"))
  expect(setTheme).toHaveBeenCalledWith("galaxy")
})