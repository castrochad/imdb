# ...

if not selected_info.empty:
    # ... (exibir informações do filme)

    # Verificar se os dados de Gross Worldwide, Gross in US & Canada e Opening Weekend Gross estão disponíveis
    if 'Gross worldwide' in selected_info.columns and 'Gross in US & Canada' in selected_info.columns and 'Opening Weekend Gross in US & Canada' in selected_info.columns:
        gross_values = selected_info[['Gross worldwide', 'Gross in US & Canada', 'Opening Weekend Gross in US & Canada']].values[0]
        labels = ['Gross worldwide', 'Gross in US & Canada', 'Opening Weekend Gross']

        # Verificar se há valores nulos
        if not pd.isnull(gross_values).any():
            fig, ax = plt.subplots()
            ax.pie(gross_values, labels=labels, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.pyplot(fig)
        else:
            st.write('Há valores ausentes para criar o gráfico de pizza.')
    else:
        st.write('As colunas necessárias para criar o gráfico não estão presentes no conjunto de dados.')
else:
    st.write('Nenhuma informação disponível para o filme selecionado.')
