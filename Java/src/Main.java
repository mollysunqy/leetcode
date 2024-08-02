public class Main {
    public static void main(String[] args) {
        SearchSuggestionsSystem s = new SearchSuggestionsSystem();
        String[] p = {"mobile","mouse","moneypot","monitor","mousepad"};
        s.suggestedProducts(p,"mouse");
    }
}